#将抓取的家谱变成横截面数据和面板数据
import os


## 1.1.1 家谱横截面数据
import pandas as pd

#Step 1: 读取数据
import os
import pandas as pd
data_folder = '../data/processed'
df = pd.read_csv(f"{data_folder}/clans/1.3_genealogy_clean.csv")

# Step 2: 提取省、市信息
df_cross = df[['省', '市']].dropna()
df_cross.columns = ['province', 'city']

# Step 3: 分组统计横截面数据
cross_section = df_cross.groupby(['province', 'city']).size().reset_index(name='total_genealogy_count')

# Step 4: 保存横截面数据
cross_section.to_csv(f"{data_folder}/clans/2.1.1 genealogy_cross-section_2023.csv", index=False)

## 1.1.2 家谱面板数据
import os
import pandas as pd

# Step 1: 读取清洗后的族谱数据
data_folder = '../data/processed'
df = pd.read_csv(f"{data_folder}/clans/1.3_genealogy_clean.csv")

# Step 2: 提取省、市、年份
df_panel = df[['省', '市', '时间']].dropna()
df_panel.columns = ['province', 'city', 'year']

# Step 3: 分组计数得到面板数据
panel_count = df_panel.groupby(['province', 'city', 'year']).size().reset_index(name='genealogy_count')

# Step 4: 保存结果
panel_count.to_csv(f"{data_folder}/clans/2.1.2 genealogy_panel.csv", index=False)

## 1.1.3 家谱面板累计数据
import pandas as pd
import os

# === Step 1: 设置路径（请根据你本地路径修改） ===
data_folder = "../data/processed/clans"
input_path = os.path.join(data_folder, "2.1.2 genealogy_panel.csv")
output_path = os.path.join(data_folder, "2.1.3 genealogy_panel.csv")

# === Step 2: 读取面板数据（每年新增族谱数） ===
df_panel = pd.read_csv(input_path)

# 清理字段空格，统一格式
df_panel['province'] = df_panel['province'].str.strip()
df_panel['city'] = df_panel['city'].str.strip()

# 按省市+年份排序，并计算累计总和
df_panel = df_panel.sort_values(by=['province', 'city', 'year']).reset_index(drop=True)
df_panel['genealogy_total_history'] = df_panel.groupby(['province', 'city'])['genealogy_count'].cumsum()

# === Step 3: 保存结果 ===
os.makedirs(os.path.dirname(output_path), exist_ok=True)
df_panel.to_csv(output_path, index=False, encoding='utf-8-sig')



## 1.2 农业转型数据

## 1.2.1 家庭农场
import pandas as pd
import os

# 设置输入输出路径
input_path = "../data/raw/city-level/地级市家庭农场数量2013-2023.xlsx"  # 可根据实际路径修改
output_path = "../data/processed/indicators of agricultural transformation/family_farms_panel.csv"

# Step 1: 读取原始 Excel 文件
df = pd.read_excel(input_path)

# Step 2: 选择并重命名核心字段
df_clean = df[['year', '所属省份', '城市名', '成立家庭农场(个)', '清退家庭农场(个)', '家庭农场存量(个)']].copy()
df_clean.columns = [
    'year',         # 年份
    'province',     # 省份
    'city',         # 地级市名称
    'new_farms',    # 新增家庭农场数量
    'closed_farms', # 注销/清退家庭农场数量
    'farm_stock'    # 年末家庭农场总数（存量）
]

# Step 3: 保存为 CSV 文件（防止中文乱码）
os.makedirs(os.path.dirname(output_path), exist_ok=True)
df_clean.to_csv(output_path, index=False, encoding='utf-8-sig')

## 1.2.2 农民专业合作社

import pandas as pd
import os

# 设置输入输出路径
input_path = "../data/raw/city-level/地级市农民专业合作社数量2007-2023.xlsx"  # 可根据实际路径修改
output_path = "../data/processed/indicators of agricultural transformation/city_agro_coops_panel.csv"

# Step 1: 读取原始 Excel 文件
df = pd.read_excel(input_path)

# 精选并重命名字段
df_clean = df[['year', '所属省份', '城市名', '成立合作社数(个)', '清退合作社数(个)', '当年合作社存量数(个)']].copy()
df_clean.columns = [
    'year',
    'province',
    'city',
    'new_coops',       # 新登记合作社
    'closed_coops',    # 注销/清退合作社
    'coop_stock'       # 合作社存量
]

# 保存为 CSV
os.makedirs(os.path.dirname(output_path), exist_ok=True)
df_clean.to_csv(output_path, index=False, encoding='utf-8-sig')

df_clean.head()


## 1.3 各城市面板数据

## 1.3.1 原版
import pandas as pd
import os

input_path = "../data/raw/city-level/中国城市数据库6.0版.xlsx"  # 可根据实际路径修改
output_path = "../data/processed/cities/cities database_panel.csv"
# 自动创建输出目录（如果不存在）
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# === Step 2: 读取 Excel 文件 ===
df = pd.read_excel(input_path)

# === Step 3: 保存为 CSV，保留中文变量名 ===
df.to_csv(output_path, index=False, encoding='utf-8-sig')

## 1.3.2 线性插值
import pandas as pd
import os

input_path = "../data/raw/city-level/中国城市数据库6.0版.xlsx"  # 可根据实际路径修改
output_path = "../data/processed/cities/cities database_interpolated_panel.csv"

# === Step 2: 读取 Excel 的第二张工作表（索引从0开始） ===
df = pd.read_excel(input_path, sheet_name=1)

# === Step 3: 保存为 CSV 文件（保持原列名） ===
df.to_csv(output_path, index=False, encoding='utf-8-sig')

## 1.3.3 各城市ARIMA填补面板数据
import pandas as pd
import os

input_path = "../data/raw/city-level/中国城市数据库6.0版.xlsx"  # 可根据实际路径修改
output_path = "../data/processed/cities/cities database_ARIMA_panel.csv"

# === Step 2: 读取 Excel 的第二张工作表（索引从0开始） ===
df = pd.read_excel(input_path, sheet_name=2)

# === Step 3: 保存为 CSV 文件（保持原列名） ===
df.to_csv(output_path, index=False, encoding='utf-8-sig')
