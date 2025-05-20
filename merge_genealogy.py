import os
import pandas as pd

# ==== 设置参数 ====
folder = "."  # 当前目录
output_file = "家谱_总表_合并.csv"

# ==== 查找所有CSV文件 ====
csv_files = [f for f in os.listdir(folder) if f.startswith("家谱_第") and f.endswith(".csv")]
csv_files.sort()  # 按文件名顺序排序

print(f"📂 找到 {len(csv_files)} 个待合并的 CSV 文件")

# ==== 读取并合并 ====
df_list = []

for file in csv_files:
    try:
        df = pd.read_csv(os.path.join(folder, file), encoding="utf-8-sig")
        df["来源文件"] = file  # 可选：加一列记录来源文件
        df_list.append(df)
    except Exception as e:
        print(f"❌ 读取文件 {file} 时失败：{e}")

# ==== 合并 & 去重 ====
if df_list:
    df_total = pd.concat(df_list, ignore_index=True)
    df_total.drop_duplicates(inplace=True)

    df_total.to_csv(output_file, index=False, encoding="utf-8-sig")
    print(f"✅ 合并完成，共 {len(df_total)} 条记录，已保存为：{output_file}")
else:
    print("⚠️ 没有读取到任何有效数据，未生成合并文件")
