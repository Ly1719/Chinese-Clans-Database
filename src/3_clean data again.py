# import pandas as pd
# import os
#
# input_path = '../data/final/1.1_merged_interpolated_panel.csv'
# output_path = input_path  # 覆盖保存
#
# df = pd.read_csv(input_path)
#
# # 要插入的指标列
# cols_to_insert = [
#     'genealogy_count', 'genealogy_total_history',
#     'new_coops', 'closed_coops', 'coops_stock',
#     'new_farms', 'closed_farms', 'farms_stock'
# ]
# cols_to_insert = [col for col in cols_to_insert if col in df.columns]
#
# # 保存原列数据并删除
# col_data = df[cols_to_insert].copy()
# df.drop(columns=cols_to_insert, inplace=True)
#
# # 找到 city_code 位置并插入
# if 'city_code' not in df.columns:
#     raise ValueError("❌ 列 'city_code' 不存在，请检查 CSV 文件列名")
# pos = df.columns.get_loc('city_code') + 1
# for i, col in enumerate(cols_to_insert):
#     df.insert(pos + i, col, col_data[col])
#
# # 覆盖保存
# os.makedirs(os.path.dirname(output_path), exist_ok=True)
# df.to_csv(output_path, index=False, encoding='utf-8-sig')
#
# print(f"✅ 已覆盖保存文件: {os.path.abspath(output_path)}")

#3.2去除累计列
# import pandas as pd
# import os
#
# file_path = '../data/final/1.1_merged_interpolated_panel.csv'
#
# # 读取
# df = pd.read_csv(file_path)
#
# # 如果存在这一列则删除
# if 'genealogy_total_history' in df.columns:
#     df = df.drop(columns=['genealogy_total_history'])
#
# df.to_csv(file_path, index=False, encoding='utf-8-sig')


#3.3去除累计列
# import pandas as pd
# import os
#
# # 文件路径
# panel_path = '../data/final/1.1_merged_interpolated_panel.csv'
# cross_path = '../data/processed/clans/2.1.1 genealogy_cross-section_2023.csv'
#
# # 读取数据
# df_panel = pd.read_csv(panel_path)
# df_cross = pd.read_csv(cross_path)
#
# # Step 1: 删除 genealogy_total_history 列（如果存在）
# if 'genealogy_total_history' in df_panel.columns:
#     df_panel.drop(columns=['genealogy_total_history'], inplace=True)
#
# # Step 2: 清理省市列（去掉空格）
# for df in [df_panel, df_cross]:
#     for col in ['province', 'city']:
#         if col in df.columns:
#             df[col] = df[col].astype(str).str.strip()
#
# # Step 3: 把 total_genealogy_count 改成 genealogy_total_2023
# df_cross.rename(columns={'total_genealogy_count': 'genealogy_total_2023'}, inplace=True)
#
# # Step 4: 合并横截面数据（只按省市匹配）
# df_panel = df_panel.merge(
#     df_cross[['province', 'city', 'genealogy_total_2023']],
#     on=['province', 'city'], how='left'
# )
#
# # Step 5: 将同一城市的 2023 值填充到所有年份
# df_panel['genealogy_total_2023'] = df_panel.groupby(['province', 'city'])['genealogy_total_2023'].transform('first')
#
# # Step 6: 保存（覆盖原文件）
# df_panel.to_csv(panel_path, index=False, encoding='utf-8-sig')
# print(f"✅ 已将 2023 横截面总数加入，并保存到 {panel_path}")


#3.4 保留2013年后的数据
# import pandas as pd
# import os
#
# # 输入输出路径
# input_path = '../data/final/1.1_merged_interpolated_panel.csv'
# output_path = '../data/final/1.2_merged_interpolated_panel_after2013.csv'
#
# # 读取数据
# df = pd.read_csv(input_path)
#
# # 去掉省市名空格
# df['province'] = df['province'].astype(str).str.strip()
# df['city'] = df['city'].astype(str).str.strip()
#
# # 只保留 2013 年及以后的数据
# df = df[df['year'] >= 2013].copy()
#
# # 保存到新文件
# os.makedirs(os.path.dirname(output_path), exist_ok=True)
# df.to_csv(output_path, index=False, encoding='utf-8-sig')
#
# print(f"✅ 已生成新文件: {output_path}")


## 3.5 统计每个城市历年的累计家谱数量_after 2013
import pandas as pd

# 读取数据
file_path = '../data/final/1.2_merged_interpolated_panel_after2013.csv'
df = pd.read_csv(file_path)

# 去掉省市名空格
df['province'] = df['province'].astype(str).str.strip()
df['city'] = df['city'].astype(str).str.strip()

# 生成累计列 genealogy_total_history
df['genealogy_cumulative_count'] = (
    df.sort_values(['province', 'city', 'year'])
      .groupby(['province', 'city'])['genealogy_count']
      .cumsum()
)

# 保存覆盖原文件
df.to_csv(file_path, index=False, encoding='utf-8-sig')
