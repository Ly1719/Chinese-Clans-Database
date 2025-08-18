import pandas as pd
import os

# 路径
input_path_1 = '../data/processed/cities/cities database_interpolated_panel.csv'
input_path_2 = '../data/processed/clans/2.1.3 genealogy_panel.csv'
input_path_3 = '../data/processed/indicators of agricultural transformation/city_agro_coops_panel.csv'
input_path_4 = '../data/processed/indicators of agricultural transformation/family_farms_panel.csv'
output_path  = '../data/final/1.1_merged_interpolated_panel.csv'

# 读取
df_cities    = pd.read_csv(input_path_1)
df_genealogy = pd.read_csv(input_path_2)
df_coops     = pd.read_csv(input_path_3)
df_farms     = pd.read_csv(input_path_4)

# 清理列名空格（防止 KeyError）
for df in [df_cities, df_genealogy, df_coops, df_farms]:
    df.columns = df.columns.str.strip()
    if 'province' in df.columns:
        df['province'] = df['province'].astype(str).str.strip()
    if 'city' in df.columns:
        df['city'] = df['city'].astype(str).str.strip()
    if 'year' in df.columns:
        df['year'] = pd.to_numeric(df['year'], errors='coerce').astype('Int64')

# 重命名关键指标
if 'genealogy_count' in df_genealogy.columns:
    df_genealogy.rename(columns={'genealogy_count': 'genealogy_count_new'}, inplace=True)
if 'coop_stock' in df_coops.columns:
    df_coops.rename(columns={'coop_stock': 'coops_stock'}, inplace=True)
if 'farm_stock' in df_farms.columns:
    df_farms.rename(columns={'farm_stock': 'farms_stock'}, inplace=True)

# 合并
merged = (df_cities
          .merge(df_genealogy, on=['province','city','year'], how='left')
          .merge(df_coops,     on=['province','city','year'], how='left')
          .merge(df_farms,     on=['province','city','year'], how='left'))

os.makedirs(os.path.dirname(output_path), exist_ok=True)
merged.to_csv(output_path, index=False, encoding='utf-8-sig')


