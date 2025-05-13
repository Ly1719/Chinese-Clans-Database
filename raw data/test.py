import requests
from bs4 import BeautifulSoup
import pandas as pd

# 请求头信息
header = {
    'Referer': 'https://www.google.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

# 初始化存储家谱信息的字典
geneologies_info = {'name': [], 'information': []}

# 目标 URL


url = f"https://jiapu.library.sh.cn/#/genealogyCenter"
response = requests.get(url, headers=header)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')
result = soup.find_all(name='div', class_='_179EwAVr5OF45JQ67B1bVg')
print(response.text)
    # 遍历每个 div，查找所有的 <dt> 和 <dd> 标签并提取内容
for div in result:
    info_list = div.find_all(name='span',class_='_2Z0AaaOL0KtTMyqlIhJ-09')
    print(info_list.test)

#         for name in name_list:
#             cleaned_name = name.text.strip()  # 去除多余的空白
#             geneologies_info['name'].append(cleaned_name)  # 添加到字典
#             print(cleaned_name)  # 打印名称
#
#         # 提取所有的信息（<dd> 标签）
#         information_list = div.find_all(name='dd')
#         for information in information_list:
#             cleaned_information = information.text.strip()  # 去除多余的空白
#             geneologies_info['information'].append(cleaned_information)  # 添加到字典
#             print(cleaned_information)  # 打印信息
#
#     # 将数据存储到 DataFrame 并保存为 Excel 文件
#     data = pd.DataFrame(geneologies_info['name'])
#     data.to_excel('./1.xlsx', index=False)
#
#     data = pd.DataFrame(geneologies_info['information'])
#     data.to_excel('./2.xlsx', index=False)
#
