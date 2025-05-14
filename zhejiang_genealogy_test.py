import tabnanny
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



#test 1

# CHROMEDRIVER_PATH = r"C:\Users\user\Desktop\thesis_data\chromedriver-win64\chromedriver.exe"
#
# options = Options()
# options.add_argument("--headless")
# options.add_argument("--disable-gpu")
# options.add_argument("--no-sandbox")
#
# service = Service(CHROMEDRIVER_PATH)
# driver = webdriver.Chrome(service=service, options=options)
#
# driver.get("https://jiapu.library.sh.cn/#/genealogyCenter")
# print("✅ 正在等待页面加载...")
#
# # 等待 class 为 genealogy-title 的元素出现（最多等10秒）
# try:
#     WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CLASS_NAME, "genealogy-title"))
#     )
# except:
#     print("❌ 页面加载失败，未找到任何家谱标题")
#     driver.quit()
#     exit()
#
# # 提取所有标题
# titles = []
# elements = driver.find_elements(By.CLASS_NAME, "genealogy-title")
# for elem in elements:
#     text = elem.text.strip()
#     if text:  # 过滤空字符串
#         titles.append(text)
#         print("📖", text)
#
# # 保存为 Excel
# df = pd.DataFrame({'家谱标题': titles})
# df.to_excel("第一页家谱标题.xlsx", index=False)
# print("✅ 提取完成，共提取", len(titles), "条记录")
# driver.quit()
#
#
# print(driver.page_source[:1000])  # 打印前1000个字符
# driver.get("https://jiapu.library.sh.cn/#/genealogyCenter")
# time.sleep(5)
# print(driver.page_source[:1000])  # 打印页面源码的前1000字符

#test 2
#
# # 设置 chromedriver 路径
# CHROMEDRIVER_PATH = r"C:\Users\user\Desktop\thesis_data\chromedriver-win64\chromedriver.exe"
#
# # 启动浏览器（无头）
# options = Options()
# options.add_argument("--headless")
# options.add_argument("--disable-gpu")
# options.add_argument("--no-sandbox")
#
# service = Service(CHROMEDRIVER_PATH)
# driver = webdriver.Chrome(service=service, options=options)
#
# # 打开家谱中心网页
# driver.get("https://jiapu.library.sh.cn/#/genealogyCenter")
# print("✅ 成功打开网页，等待数据加载...")
# time.sleep(5)  # 等待 JavaScript 渲染
#
# driver.save_screenshot("genealogy_debug.png")
# print("📸 已截图保存为 genealogy_debug.png")
#
# # 关闭浏览器
# driver.quit()

#test4
# CHROMEDRIVER_PATH = r"C:\Users\user\Desktop\thesis_data\chromedriver-win64\chromedriver.exe"
#
# options = Options()
# options.add_argument("--headless")
# options.add_argument("--disable-gpu")
# options.add_argument("--no-sandbox")
#
# service = Service(CHROMEDRIVER_PATH)
# driver = webdriver.Chrome(service=service, options=options)
#
# driver.get("https://jiapu.library.sh.cn/#/genealogyCenter")
# print("✅ 成功打开网页，等待加载...")
# time.sleep(5)
#
# # 点击“确定”按钮
# from selenium.webdriver.common.action_chains import ActionChains
#
# # 等待“确定”按钮出现
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# try:
#     confirm_span = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, "//span[text()='确定']"))
#     )
#     ActionChains(driver).move_to_element(confirm_span).click().perform()
#     print("✅ 已用 ActionChains 成功模拟点击‘确定’按钮")
# except Exception as e:
#     print("❌ 没有成功点击‘确定’：", e)
#     driver.save_screenshot("click_failed.png")
#     driver.quit()
#     exit()
#
# time.sleep(5)  # 等待家谱数据加载
# driver.save_screenshot("after_confirm_click.png")
#
# # 提取数据字段：谱名，责任者，姓氏，撰修时间，堂号，家谱简介
# data = []
# elements = driver.find_elements(By.XPATH, "//a[@target='_blank']")
#
# for el in elements:
#     spans = el.find_elements(By.TAG_NAME, "span")
#     if len(spans) < 6:
#         continue  # 数据不全则跳过
#     data.append({
#         "谱名": spans[0].text.strip(),
#         "责任者": spans[1].text.strip(),
#         "姓氏": spans[2].text.strip(),
#         "撰修时间": spans[3].text.strip(),
#         "堂号": spans[4].text.strip(),
#         "家谱简介": spans[5].text.strip(),
#         "详情链接": el.get_attribute("href")
#     })
#
# # 保存结果
# df = pd.DataFrame(data)
# df.to_excel("家谱第一页详细数据.xlsx", index=False)
# print("✅ 已提取", len(df), "条记录，保存为 家谱第一页详细数据.xlsx")
#
# driver.quit()
#test 5
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import time

CHROMEDRIVER_PATH = r"C:\Users\user\Desktop\thesis_data\chromedriver-win64\chromedriver.exe"

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://jiapu.library.sh.cn/#/genealogyCenter")
print("✅ 成功打开网页，等待加载...")
time.sleep(5)

# 点击“确定”按钮
from selenium.webdriver.common.action_chains import ActionChains

# 等待“确定”按钮出现
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    confirm_span = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[text()='确定']"))
    )
    ActionChains(driver).move_to_element(confirm_span).click().perform()
    print("✅ 已用 ActionChains 成功模拟点击‘确定’按钮")
except Exception as e:
    print("❌ 没有成功点击‘确定’：", e)
    driver.save_screenshot("click_failed.png")
    driver.quit()
    exit()

time.sleep(5)  # 等待家谱数据加载
driver.save_screenshot("after_confirm_click.png")

# 提取数据字段：谱名，责任者，姓氏，撰修时间，堂号，家谱简介
data = []
elements = driver.find_elements(By.XPATH, "//a[starts-with(@href, '#/GenealogySummary:')]")

for el in elements:
    spans = el.find_elements(By.TAG_NAME, "span")
    if len(spans) < 6:
        continue

    # 提取文字，包括嵌套<i>的内容
    def safe_text(span):
        return span.get_attribute("innerText").strip()

    data.append({
        "谱名": safe_text(spans[0]),
        "责任者": safe_text(spans[1]),
        "姓氏": safe_text(spans[2]),
        "撰修时间": safe_text(spans[3]),
        "堂号": safe_text(spans[4]),
        "家谱简介": safe_text(spans[5]),
        "详情链接": "https://jiapu.library.sh.cn/" + el.get_attribute("href").lstrip("#/")
    })

# 保存结果
df = pd.DataFrame(data)
df.to_csv("家谱第一页六字段.csv", index=False, encoding="utf-8-sig")
print("✅ 共提取", len(df), "条家谱记录，已保存为 CSV 文件")

driver.quit()





















































































































































































































































































































































































































































