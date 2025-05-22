import pandas as pd
import re

# === 读取文件 ===
df = pd.read_csv("data_genealogy_cleaned_gross.csv", encoding="utf-8-sig")

# === 提取撰修时间中的纯年份 ===
def clean_time_numeric(raw):
    if pd.isna(raw):
        return None
    text = str(raw)

    # 括号中优先提取4位数字年份
    match_year_in_brackets = re.search(r"[（(](\d{4})[）)]", text)
    if match_year_in_brackets:
        return match_year_in_brackets.group(1)

    # 查找一般4位年份
    match_year = re.search(r"(\d{4})", text)
    if match_year:
        return match_year.group(1)

    # 若无年份，则保留原始描述
    return text

# 应用清洗函数
df["撰修时间_纯数字"] = df["撰修时间"].apply(clean_time_numeric)

# 可选保存结果
df.to_csv("data_final_genealogy.csv", index=False, encoding="utf-8-sig")


