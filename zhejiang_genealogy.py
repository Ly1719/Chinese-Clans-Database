import requests #用于发送 HTTP 请求，从网页获取 HTML 内容。
import pandas as pd #用于处理和存储结构化数据，比如表格、DataFrame、保存为 Excel 等。
import re #导入正则表达式模块，用于从字符串中提取特定内容（如 URL 中的数字、姓氏等）。
import matplotlib #Matplotlib 是 Python 的绘图库，一般用于可视化数据。
import os #操作文件路径、目录等功能（如创建文件夹、判断文件是否存在等）。
import io #操作内存中的文件对象，比如把网络下载的数据当成文件处理（适用于解压、Excel 处理等）。
import matplotlib.pyplot as plt #Matplotlib 的子模块，专门用于绘图（柱状图、折线图、词云图等）。
import time #用于添加延迟，防止被网站屏蔽。
from bs4 import BeautifulSoup #导入 BeautifulSoup 库，用于解析 HTML 网页，从中提取信息。
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# ✅ 设置 ChromeDriver 路径和要抓的页数范围
CHROMEDRIVER_PATH = r"C:\Users\user\Desktop\thesis_data\chromedriver-win64\chromedriver.exe"
start_page = 1      # 从第几页开始
num_pages = 5      # 抓取几页（例如：抓1~5页）

# ✅ 初始化浏览器
options = Options()
# options.add_argument("--headless")  # 调试阶段建议注释掉
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://jiapu.library.sh.cn/#/genealogyCenter")
print("✅ 成功打开网页，等待加载...")
time.sleep(5)

# ✅ 点击“确定”按钮以加载家谱列表
try:
    confirm_span = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[text()='确定']"))
    )
    ActionChains(driver).move_to_element(confirm_span).click().perform()
    print("✅ 已点击‘确定’，等待家谱数据加载...")
except Exception as e:
    print("❌ 点击失败：", e)
    driver.quit()
    exit()

# ✅ 等待第一页家谱加载
WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "//a[starts-with(@href, '#/GenealogySummary:')]"))
)

# ✅ 如果不是从第1页开始，先跳页
if start_page > 1:
    try:
        input_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='text']"))
        )
        driver.execute_script("arguments[0].click();", input_box)
        time.sleep(1)
        input_box.clear()
        input_box.send_keys(str(start_page))
        input_box.send_keys(Keys.ENTER)
        print(f"🔁 已跳转至第 {start_page} 页")
        time.sleep(5)
    except Exception as e:
        print("❌ 跳转页失败：", e)
        driver.quit()
        exit()

# ✅ 抓取数据
all_data = []

for page in range(start_page, start_page + num_pages):
    print(f"📄 正在抓取第 {page} 页...")
    time.sleep(2)

    elements = driver.find_elements(By.XPATH, "//a[starts-with(@href, '#/GenealogySummary:')]")

    for el in elements:
        spans = el.find_elements(By.TAG_NAME, "span")
        if len(spans) < 6:
            continue

        def safe_text(span):
            return span.get_attribute("innerText").strip()

        all_data.append({
            "谱名": safe_text(spans[0]),
            "责任者": safe_text(spans[1]),
            "姓氏": safe_text(spans[2]),
            "撰修时间": safe_text(spans[3]),
            "堂号": safe_text(spans[4]),
            "家谱简介": safe_text(spans[5]),
            "详情链接": "https://jiapu.library.sh.cn/" + el.get_attribute("href").lstrip("#/")
        })

    # ✅ 模拟点击“下一页”
    try:
        next_button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(), '下一页')]"))
        )
        driver.execute_script("arguments[0].click();", next_button)
    except Exception as e:
        print("⚠️ 翻页失败：", e)
        break

# ✅ 保存结果
df = pd.DataFrame(all_data)
df.to_csv(f"家谱_第{start_page}_页起_共{num_pages}页.csv", index=False, encoding="utf-8-sig")
print(f"✅ 共提取 {len(df)} 条记录，已保存为 CSV 文件")

driver.quit()


























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



