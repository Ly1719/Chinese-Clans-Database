import pandas as pd

# 读取原始文件，不使用第一行作为列名
df_raw = pd.read_csv("data_merge_genealogy.csv", header=None)

# 将第一行设为列名
df_raw.columns = df_raw.iloc[0]

# 删除第一行数据（原来是标题），重置索引
df_filter = df_raw.drop(index=0).reset_index(drop=True)

# 删除指定列
df = df_filter.drop(columns=["详情链接", "堂号", "家谱简介"])

# 将“谱名”列移到最前面
columns = list(df.columns)
columns.insert(0, columns.pop(columns.index("谱名")))
df = df[columns]

# 保存为新文件（可选）
df.to_csv("data_filter_genealogy.csv", index=False, encoding="utf-8-sig")

