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
elements = driver.find_elements(By.XPATH, "//a[@target='_blank']")

for el in elements:
    spans = el.find_elements(By.TAG_NAME, "span")
    texts = [s.text.strip() for s in spans if s.text.strip()]
    if not texts:
        continue

    title = texts[0]
    responsibility = ""
    surname = ""
    edit_time = ""
    hall = ""
    intro = ""

    for t in texts[1:]:
        if not responsibility:
            responsibility = t
        elif not surname and ("氏" in t and len(t) <= 4):
            surname = t
        elif not edit_time and ("年" in t or "民国" in t or t.isdigit()):
            edit_time = t
        elif not hall and ("堂" in t or "堂号" in t):
            hall = t
        elif not intro:
            intro = t  # 剩下的作为简介

    data.append({
        "谱名": title,
        "责任者": responsibility,
        "姓氏": surname,
        "撰修时间": edit_time,
        "堂号": hall,
        "家谱简介": intro,
        "详情链接": el.get_attribute("href")
    })


# 保存结果
df = pd.DataFrame(data)
df.to_excel("家谱第一页详细数据.xlsx", index=False)
print("✅ 已提取", len(df), "条记录，保存为 家谱第一页详细数据.xlsx")

driver.quit()

