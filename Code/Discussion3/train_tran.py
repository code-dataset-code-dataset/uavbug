import pandas as pd
import numpy as np
from collections import Counter
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
from imblearn.over_sampling import SMOTE, RandomOverSampler

# =================配置区域=================
file_path = r'..\..\Dataset\MetricsData.xlsx'


# =========================================

def train_cross_project(file_path):
    # 1. 读取数据
    try:
        df = pd.read_excel(file_path)
    except FileNotFoundError:
        print(f"错误：找不到文件 {file_path}")
        return

    # 定义列名
    # 注意：repo_name 在这里暂时保留，用于划分，划分后再删除
    features_to_drop = ['Issue', 'repo_name', 'Author Username', 'Issue Date']
    label_columns = ['Is the Bug Reproduced?']

    # 2. 数据清洗
    df = df.dropna(subset=label_columns)

    # =======================================================
    # 【核心修改】基于 repo_name 进行划分
    # =======================================================
    # 这里的字符串必须和 Excel 中的完全一致（注意大小写和空格）
    train_mask = df['repo_name'] == 'PX4-Autopilot'
    test_mask = df['repo_name'] == 'ardupilot'

    df_train = df[train_mask].copy()
    df_test = df[test_mask].copy()

    print(f"数据划分统计:")
    print(f"  - 训练集 (PX4-Autopilot): {len(df_train)} 条")
    print(f"  - 测试集 (ardupilot):     {len(df_test)} 条")

    if len(df_train) == 0 or len(df_test) == 0:
        print("错误：训练集或测试集为空。请检查 Excel 中 repo_name 列的值是否拼写正确。")
        return

    # 3. 分离特征 (X) 和 标签 (Y)
    # 此时可以安全地把 repo_name 和其他无关列删除了
    X_train = df_train.drop(columns=features_to_drop + label_columns, errors='ignore')
    Y_train_all = df_train[label_columns]

    X_test = df_test.drop(columns=features_to_drop + label_columns, errors='ignore')
    Y_test_all = df_test[label_columns]

    # 4. 特征编码 (One-Hot) 与 对齐
    print("正在进行特征编码与对齐...")
    X_train = pd.get_dummies(X_train, drop_first=True)
    X_test = pd.get_dummies(X_test, drop_first=True)

    # 【关键步骤】对齐列名
    # 确保训练集和测试集拥有完全相同的列。
    # 如果 PX4 有某列而 Ardupilot 没有，给 Ardupilot 补 0；反之亦然。
    X_train, X_test = X_train.align(X_test, join='outer', axis=1, fill_value=0)

    # 5. 缺失值填充
    # 规则：用训练集的均值去填充训练集和测试集
    imputer = SimpleImputer(strategy='mean')
    X_train = pd.DataFrame(imputer.fit_transform(X_train), columns=X_train.columns)
    X_test = pd.DataFrame(imputer.transform(X_test), columns=X_test.columns)

    # 定义模型
    models = {
        "随机森林": RandomForestClassifier(n_estimators=100, random_state=42),
    }

    # 6. 循环训练
    for target_label in label_columns:
        print(f"\n{'=' * 80}")
        print(f"正在跨项目预测标签: 【{target_label}】")

        y_train_cur = Y_train_all[target_label].values.ravel()
        y_test_cur = Y_test_all[target_label].values.ravel()

        # --- 自适应上采样 (只针对训练集 PX4) ---
        class_counts = Counter(y_train_cur)
        min_class_count = min(class_counts.values())
        print(f"训练集(PX4) 分布: {class_counts}")

        # 计算 k 值
        calculated_k = min(5, min_class_count - 2)

        if calculated_k < 1:
            print(f">>> 样本极少，使用 RandomOverSampler。")
            sampler = RandomOverSampler(random_state=42)
        else:
            print(f">>> 使用 SMOTE (k={calculated_k})。")
            sampler = SMOTE(k_neighbors=calculated_k, random_state=42)

        try:
            X_train_res, y_train_res = sampler.fit_resample(X_train, y_train_cur)
        except Exception as e:
            print(f"上采样失败 ({e})，使用原始数据。")
            X_train_res, y_train_res = X_train, y_train_cur

        # --- 标准化 ---
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train_res)
        X_test_scaled = scaler.transform(X_test)  # 使用 PX4 的分布标准来缩放 Ardupilot

        print(f"{'-' * 80}")
        print(f"{'模型名称':<20} | {'准确率':<10} | {'测试集(Ardu) F1-Score':<20}")
        print("-" * 60)

        for name, model in models.items():
            model.fit(X_train_scaled, y_train_res)
            y_pred = model.predict(X_test_scaled)
            acc = accuracy_score(y_test_cur, y_pred)

            # 这里如果不加 zero_division=0，如果Ardupilot全是某一个类，可能会报警告
            print(f"{name:<24} | {acc:.4f}")
            print(classification_report(y_test_cur, y_pred, zero_division=0))


if __name__ == "__main__":
    train_cross_project(file_path)