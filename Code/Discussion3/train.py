import pandas as pd
import numpy as np
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# ================= 引入上采样库 =================
# 确保安装了 imbalanced-learn
from imblearn.over_sampling import SMOTE, RandomOverSampler

# ===============================================

# ================= 配置区域 =================
file_path = r'..\..\Dataset\MetricsData.xlsx'


# ===========================================

def train_with_adaptive_k_smote(file_path):
    # 1. 读取数据
    try:
        df = pd.read_excel(file_path)
    except FileNotFoundError:
        print(f"错误：找不到文件 {file_path}")
        return

    # 定义列名
    excluded_columns = ['Issue', 'repo_name', 'Author Username', 'Issue Date']
    label_columns = ['Is the Bug Reproduced?']

    # 2. 数据清洗
    # 删除标签为空的行
    df = df.dropna(subset=label_columns)

    # 分离特征和标签
    X = df.drop(columns=excluded_columns + label_columns, errors='ignore')
    Y_all = df[label_columns]

    # 3. 特征预处理
    # 独热编码 (One-Hot)
    X = pd.get_dummies(X, drop_first=True)

    # 缺失值填充
    imputer = SimpleImputer(strategy='mean')
    X_imputed = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)

    # 4. 统一划分数据集 (5:5)
    # stratify=Y_all 尝试保持两个标签的组合分布一致，如果报错(因为样本太少)可以去掉 stratify 参数
    try:
        X_train_raw, X_test_raw, Y_train_all, Y_test_all = train_test_split(
            X_imputed, Y_all, test_size=0.5, random_state=42, stratify=Y_all
        )
    except ValueError:
        print("提示：样本量过小或某些类别组合只有1个样本，无法进行分层划分(Stratify)，已切换为随机划分。")
        X_train_raw, X_test_raw, Y_train_all, Y_test_all = train_test_split(
            X_imputed, Y_all, test_size=0.5, random_state=42
        )

    print(f"数据集划分完成。训练集: {len(X_train_raw)}, 测试集: {len(X_test_raw)}")

    # 定义模型字典
    models = {
        "随机森林": RandomForestClassifier(n_estimators=100, random_state=42),
    }

    # 5. 循环针对每个标签进行【动态上采样 + 训练】
    for target_label in label_columns:
        print(f"\n{'=' * 80}")
        print(f"正在处理标签: 【{target_label}】")

        # 提取当前标签的单列数据
        y_train_cur = Y_train_all[target_label].values.ravel()
        y_test_cur = Y_test_all[target_label].values.ravel()

        # 统计样本分布
        class_counts = Counter(y_train_cur)
        min_class_count = min(class_counts.values())
        print(f"原始训练集分布: {class_counts} (最少类样本数: {min_class_count})")

        # =======================================================
        # 【核心逻辑】动态设置 k_neighbors
        # 公式: k = min(5, min_class_count - 2)
        # =======================================================

        # 计算理论上的 k 值
        calculated_k = min(5, min_class_count - 2)

        # 决策逻辑：
        # SMOTE 要求 k_neighbors >= 1。
        # 如果 calculated_k < 1 (意味着 min_class_count <= 2)，则必须放弃 SMOTE，改用 RandomOverSampler。
        if calculated_k < 1:
            print(f">>> 样本极少 (N={min_class_count})，计算得 k={calculated_k}。无法使用 SMOTE。")
            print(">>> 策略切换: 使用 RandomOverSampler (随机复制)。")
            sampler = RandomOverSampler(random_state=42)
        else:
            print(f">>> 样本充足，计算得 k={calculated_k}。")
            print(f">>> 策略: 使用 SMOTE (k_neighbors={calculated_k})。")
            sampler = SMOTE(k_neighbors=calculated_k, random_state=42)

        # 执行重采样
        try:
            X_train_res, y_train_res = sampler.fit_resample(X_train_raw, y_train_cur)
            print(f"上采样后 训练集分布: {Counter(y_train_res)}")
        except Exception as e:
            print(f"!!! 上采样过程发生未知错误: {e}")
            print("!!! 将使用原始数据继续训练")
            X_train_res, y_train_res = X_train_raw, y_train_cur

        # --- 标准化 (Scaling) ---
        # 必须在上采样之后 fit
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train_res)
        X_test_scaled = scaler.transform(X_test_raw)

        print(f"{'-' * 80}")
        print(f"{'模型名称':<20} | {'准确率':<10} | {'F1-Score (Macro)':<15}")
        print("-" * 60)

        for name, model in models.items():
            # 训练
            model.fit(X_train_scaled, y_train_res)

            # 预测
            y_pred = model.predict(X_test_scaled)

            # 评估
            acc = accuracy_score(y_test_cur, y_pred)

            # 为了防止报错，我们在 print 时只显示准确率，详细报告在下面
            print(f"{name:<24} | {acc:.4f}")

            # 打印详细报告 (zero_division=0 用于消除警告)
            print(classification_report(y_test_cur, y_pred, zero_division=0))


if __name__ == "__main__":
    train_with_adaptive_k_smote(file_path)