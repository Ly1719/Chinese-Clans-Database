import pandas as pd

# === 读取你的原始面板数据 ===
df = pd.read_csv("panel_genealogy_cleaned_省市县.csv", encoding="utf-8-sig")

# === 分组统计：按省、市、年份汇总家谱数量 ===
panel_by_province_city = (
    df.groupby(["省", "市", "年份"])
      .agg({"家谱数量": "sum"})
      .reset_index()
)

# === 可选保存 ===
panel_by_province_city.to_csv("panel_genealogy_cleaned_省市.csv", index=False, encoding="utf-8-sig")
