import requests #用于发送 HTTP 请求，从网页获取 HTML 内容。
import pandas as pd #用于处理和存储结构化数据，比如表格、DataFrame、保存为 Excel 等。
import re #导入正则表达式模块，用于从字符串中提取特定内容（如 URL 中的数字、姓氏等）。
import matplotlib #Matplotlib 是 Python 的绘图库，一般用于可视化数据。
import os #操作文件路径、目录等功能（如创建文件夹、判断文件是否存在等）。
import io #操作内存中的文件对象，比如把网络下载的数据当成文件处理（适用于解压、Excel 处理等）。
import matplotlib.pyplot as plt #Matplotlib 的子模块，专门用于绘图（柱状图、折线图、词云图等）。
import time #用于添加延迟，防止被网站屏蔽。
from bs4 import BeautifulSoup #导入 BeautifulSoup 库，用于解析 HTML 网页，从中提取信息。

# # 启动 Selenium 无头模式
# options = webdriver.ChromeOptions()
# options.add_argument("--headless")
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-gpu")
#
# service = Service(CHROMEDRIVER_PATH)
# driver = webdriver.Chrome(service=service, options=options)
#
# # 打开家谱网站
# driver.get("https://jiapu.library.sh.cn/#/genealogyCenter")
# time.sleep(5)  # 等待 JavaScript 渲染完成
#
# # 抓取第一页的家谱标题
# titles = []
# elements = driver.find_elements(By.CLASS_NAME, "genealogy-title")
# for elem in elements:
#     titles.append(elem.text)
#     print(elem.text)
#
# # 关闭浏览器
# driver.quit()
#
# # 保存结果到 Excel
# df = pd.DataFrame({'标题': titles})
# df.to_excel("家谱标题示例.xlsx", index=False)
# print("✅ 数据已保存为 Excel 文件")
#






















# header = {
#     'Referer': 'https://jiapu.library.sh.cn/#/genealogyCenter',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}
# # 这个字典用于设置请求头，模拟“浏览器访问行为”，可以绕过反爬虫机制。
# Referer 告诉网站你是从哪个页面跳转来的；
# User-Agent 告诉服务器你使用的是什么浏览器

# def get_genealogy_data(pages=10):
#     all_data = []
#     for page in range(1, pages + 1):
#         url = f'https://jiapu.library.sh.cn/api/genealogy/list?page={page}&limit=20'
#         response = requests.get(url, headers=header)
#         if response.status_code != 200:
#             print(f"Failed to fetch page {page}")
#             continue
#         json_data = response.json()
#         for item in json_data.get('data', []):
#             all_data.append({
#                 'ID': item.get('id'),
#                 '标题': item.get('title'),
#                 '姓氏': item.get('surname'),
#                 '作者': item.get('creator'),
#                 '地区': item.get('region'),
#                 '出版时间': item.get('publishTime')
#             })
#         print(f"Page {page} done.")
#         time.sleep(1)  # 防止请求太快被封
#
#     df = pd.DataFrame(all_data)
#     df.to_excel("genealogy_data.xlsx", index=False)
#     print("爬取完成，已保存为 genealogy_data.xlsx")
#
# # 启动爬虫
# get_genealogy_data(pages=20)



