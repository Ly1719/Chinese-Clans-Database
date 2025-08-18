import pandas as pd

# === 读取原始面板数据 ===
df = pd.read_csv("panel_genealogy_cleaned_省市县.csv", encoding="utf-8-sig")

# === 按省和年份分组统计家谱数量 ===
panel_by_province = (
    df.groupby(["省", "年份"])
      .agg({"家谱数量": "sum"})
      .reset_index()
)

# === 可选保存结果 ===
panel_by_province.to_csv("panel_genealogy_cleaned_省.csv", index=False, encoding="utf-8-sig")

