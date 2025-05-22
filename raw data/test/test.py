from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

CHROMEDRIVER_PATH = r"C:\Users\user\Desktop\thesis_data\chromedriver-win64\chromedriver.exe"
NUM_PAGES = 2  # 抓取页数，可自定义

options = Options()
# options.add_argument("--headless")  # 建议初次调试时可注释掉
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://jiapu.library.sh.cn/#/genealogyCenter")
print("✅ 成功打开网页，等待加载...")
time.sleep(5)

# 点击“确定”按钮
try:
    confirm_span = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[text()='确定']"))
    )
    ActionChains(driver).move_to_element(confirm_span).click().perform()
    print("✅ 已点击‘确定’，等待家谱数据加载...")
except Exception as e:
    print("❌ 无法点击‘确定’按钮:", e)
    driver.quit()
    exit()

# 等待第一页加载
WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "//a[starts-with(@href, '#/GenealogySummary:')]"))
)

# 全部记录
all_data = []

for page in range(NUM_PAGES):
    print(f"📄 正在抓取第 {page+1} 页...")
    time.sleep(3)

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

    # 点击“下一页”
    try:
        next_button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(), '下一页')]"))
        )
        driver.execute_script("arguments[0].click();", next_button)
        print(f"➡️ 点击了第 {page + 1} 页的‘下一页’按钮")
    except Exception as e:
        print("⚠️ 下一页点击失败或按钮未找到：", e)
        break

# 保存为 CSV 文件
df = pd.DataFrame(all_data)
df.to_csv("家谱多页数据.csv", index=False, encoding="utf-8-sig")
print(f"✅ 共提取 {len(df)} 条记录，已保存为 CSV 文件：家谱多页数据.csv")

driver.quit()

