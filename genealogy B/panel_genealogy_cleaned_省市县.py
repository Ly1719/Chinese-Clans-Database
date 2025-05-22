import pandas as pd

# 读取原始面板数据文件
df = pd.read_csv("panel_genealogy_省市县.csv", encoding="utf-8-sig")

# 定义直辖市名称映射规则
direct_cities = {
    "北京": "北京市",
    "北京市": "北京市",
    "上海": "上海市",
    "上海市": "上海市",
    "重庆": "重庆市",
    "重庆市": "重庆市",
    "天津": "天津市",
    "天津市": "天津市"
}

# 替换“省”和“市”列中的名称为统一规范
df["省"] = df["省"].replace(direct_cities)
df["市"] = df["市"].replace(direct_cities)

# 找出“省”为四大直辖市的行，并将“市”字段设置为与“省”一致
direct_city_names = ["北京市", "上海市", "重庆市", "天津市"]
df.loc[df["省"].isin(direct_city_names), "市"] = df.loc[df["省"].isin(direct_city_names), "省"]

df.to_csv("panel_genealogy_cleaned_省市县.csv", index=False, encoding="utf-8-sig")
