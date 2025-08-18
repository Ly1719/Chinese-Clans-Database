import pandas as pd

# === 读取文件 ===
df = pd.read_csv("../genealogy A/data_final_genealogy.csv", encoding="utf-8-sig")

# === 提取年份 ===
# 确保时间列是字符串类型
df["时间"] = df["时间"].astype(str)

# 提取 4 位数字年份（如 1948）
df["年份"] = df["时间"].str.extract(r"(\d{4})")

# 删除没有年份的数据
df = df.dropna(subset=["年份"])

# 将年份转换为整数
df["年份"] = df["年份"].astype(int)

# === 分组统计为面板数据 ===
panel_df = df.groupby(["省", "市", "县", "年份"]).size().reset_index(name="家谱数量")

# === 可选：保存结果 ===
panel_df.to_csv("panel_genealogy_省市县.csv", index=False, encoding="utf-8-sig")

