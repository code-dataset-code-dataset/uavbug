import pandas as pd
from irrCAC.raw import CAC


def calculate_gwet_ac1_and_export_diff(file_path_A, file_path_B, output_diff_path="差异明细表.xlsx"):
    print(f"正在读取文件...\nA文件: {file_path_A}\nB文件: {file_path_B}")

    try:
        # 1. 读取 Excel 文件
        df_A = pd.read_excel(file_path_A, engine='openpyxl')
        df_B = pd.read_excel(file_path_B, engine='openpyxl')
        col_A, col_B = df_A.iloc[:, 2], df_B.iloc[:, 2]

        # 2. 对齐长度
        if len(col_A) != len(col_B):
            print("【提示】两个文件的行数不一致，已按较短的文件对齐。")
        min_len = min(len(col_A), len(col_B))
        col_A, col_B = col_A.iloc[:min_len], col_B.iloc[:min_len]

        # 3. 数据清洗：统一转为字符串，并将空值填为 "MISSING"
        list_A = col_A.fillna("MISSING").astype(str).tolist()
        list_B = col_B.fillna("MISSING").astype(str).tolist()

        # 4. 组装 Pandas DataFrame
        df_raters = pd.DataFrame({
            'Rater_A': list_A,
            'Rater_B': list_B
        })

        # 5. 计算 Gwet's AC1
        cac = CAC(df_raters)
        gwet_result = cac.gwet()

        # ==========================================
        # 终极容错提取：无论版本怎么变，自动抓取系数值
        # ==========================================
        est_dict = gwet_result.get('est', {})

        if 'coefficient_value' in est_dict:
            ac1_score = est_dict['coefficient_value']
        elif 'coefficient' in est_dict:
            ac1_score = est_dict['coefficient']
        else:
            # 如果键名又变了，强制打印出字典内容，并尝试提取第一个浮点数值
            print("\n【调试提示】irrCAC 库返回的原始字典数据如下：")
            print(gwet_result)
            ac1_score = list(est_dict.values())[0]

        # 6. 打印统计结果
        print("-" * 45)
        print(f"数据总比对行数: {len(df_raters)}")
        print(f"Gwet's AC1 一致性系数: {ac1_score:.4f}")
        print("-" * 45)

        # 解释结论
        if ac1_score < 0:
            interpretation = "一致性极差 (Poor)"
        elif 0 <= ac1_score <= 0.20:
            interpretation = "极低的一致性 (Slight)"
        elif 0.21 <= ac1_score <= 0.40:
            interpretation = "一般的一致性 (Fair)"
        elif 0.41 <= ac1_score <= 0.60:
            interpretation = "中等的一致性 (Moderate)"
        elif 0.61 <= ac1_score <= 0.80:
            interpretation = "高度的一致性 (Substantial)"
        else:
            interpretation = "极高/完全的一致性 (Almost perfect)"

        print(f"结论: {interpretation}")

        # 7. 附加功能：找出差异数据并导出 Excel
        diff_mask = df_raters['Rater_A'] != df_raters['Rater_B']
        df_diff = df_raters[diff_mask].copy()

        # 如果第一行是表头，那么 Pandas 的第 0 行其实对应 Excel 的第 2 行
        df_diff.insert(0, '原Excel对应行号', df_diff.index + 2)

        df_diff.to_excel(output_diff_path, index=False)
        print("-" * 45)
        print(f"【成功】已发现 {len(df_diff)} 处不一致的数据！")
        print(f"明细已自动导出至当前目录下的: {output_diff_path}")
        print("-" * 45)

    except Exception as e:
        print(f"发生错误: {e}")


# ================= 使用示例 =================
file_path_A = "A/Aall.xlsx"
file_path_B = "B/Ball.xlsx"

calculate_gwet_ac1_and_export_diff(file_path_A, file_path_B)