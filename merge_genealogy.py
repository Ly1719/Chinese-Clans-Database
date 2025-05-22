import os
import pandas as pd

# ==== 设置路径 ====
folder = "./"  # 你可以改为数据所在的具体目录路径
output_file = "data_merge_genealogy.csv"

# ==== 查找符合命名规则的文件 ====
csv_files = [f for f in os.listdir(folder) if f.startswith("家谱_第") and f.endswith(".csv")]
csv_files.sort()

# ==== 初始化合并逻辑 ====
df_list = []
common_cols = None

for file in csv_files:
    try:
        file_path = os.path.join(folder, file)
        df = pd.read_csv(file_path, encoding="utf-8-sig")

        # 更新公共列（第一次取全部，之后与前面的做交集）
        if common_cols is None:
            common_cols = set(df.columns)
        else:
            common_cols &= set(df.columns)

        df_list.append(df)
    except Exception as e:
        print(f"❌ 无法读取 {file}，错误：{e}")

# ==== 合并并保留公共列 ====
if df_list and common_cols:
    common_cols = list(common_cols)
    merged_df = pd.concat([df[common_cols] for df in df_list], ignore_index=True)
    merged_df.to_csv(output_file, index=False, encoding="utf-8-sig")
    print(f"✅ 合并完成，生成文件：{output_file}，共 {len(merged_df)} 条记录，列：{common_cols}")
else:
    print("⚠️ 没有成功读取或匹配到任何公共列，未生成文件。")

