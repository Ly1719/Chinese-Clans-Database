import pandas as pd
import re

# === Step 1: 读取数据 ===
df = pd.read_csv("data_filter_genealogy.csv", encoding="utf-8-sig")

# === Step 2: 从“谱名”中提取地址信息（括号内） ===
def extract_location(title):
    match = re.search(r"[(（](.*?)[)）]", str(title))
    return match.group(1) if match else None

df["地址"] = df["谱名"].apply(extract_location)

# === Step 3: 定义智能拆分逻辑 ===
provinces = [
    "北京", "天津", "上海", "重庆", "河北", "山西", "辽宁", "吉林", "黑龙江", "江苏", "浙江", "安徽",
    "福建", "江西", "山东", "河南", "湖北", "湖南", "广东", "海南", "四川", "贵州", "云南",
    "陕西", "甘肃", "青海", "台湾", "广西", "内蒙古", "西藏", "宁夏", "新疆", "香港", "澳门"
]
province_suffixes = ["省", "市", "自治区", "特别行政区"]
city_suffixes = ["市", "地区", "盟"]
county_suffixes = ["县", "区", "市", "旗"]

def smart_split_address(addr):
    if pd.isna(addr):
        return None, None, None
    addr = str(addr)
    if "/" in addr:
        parts = addr.split("/")
        parts = (parts + [None, None, None])[:3]
        return parts[0], parts[1], parts[2]
    for prov in provinces:
        if addr.startswith(prov):
            rest = addr[len(prov):]
            city = None
            county = None
            for suf in city_suffixes:
                if suf in rest:
                    idx = rest.find(suf)
                    city = rest[:idx+1]
                    rest = rest[idx+1:]
                    break
            for suf in county_suffixes:
                if suf in rest:
                    idx = rest.find(suf)
                    county = rest[:idx+1]
                    break
            return prov, city, county
    return addr, None, None  # fallback

# === Step 4: 应用拆分并赋值列 ===
df[["智能省", "智能市", "智能县"]] = df["地址"].apply(lambda x: pd.Series(smart_split_address(x)))

# === Step 5: 清理字段内容（去掉“省”字）===
df["智能省"] = df["智能省"].str.replace("省$", "", regex=True)
df["智能市"] = df["智能市"].str.replace("省", "", regex=True)  # 所有位置的“省”

# === Step 6: 重命名列去掉“智能”前缀 ===
df = df.rename(columns={
    "智能省": "省",
    "智能市": "市",
    "智能县": "县"
})

# === Step 7: 保存结果 ===
df.to_csv("data_genealogy_cleaned_gross.csv", index=False, encoding="utf-8-sig")


