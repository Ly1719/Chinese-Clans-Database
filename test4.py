import sys
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ==== Chrome 驱动配置 ====
CHROMEDRIVER_PATH = r"C:\Users\m1780\Desktop\Thesis\data of clans\code\chromedriver-win64\chromedriver.exe"

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://jiapu.library.sh.cn/#/genealogyCenter")
print("✅ 打开网页，加载中...")
time.sleep(5)

# ==== 点击“确定” ====
try:
    confirm_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[text()='确定']"))
    )
    ActionChains(driver).move_to_element(confirm_btn).click().perform()
    print("✅ 点击‘确定’成功")
except Exception as e:
    print("❌ ‘确定’按钮点击失败：", e)
    driver.quit()
    exit()

# ==== 跳转到指定起始页 ====
try:
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//a[starts-with(@href, '#/GenealogySummary:')]"))
    )
    if start_page > 1:
        input_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='text']"))
        )
        driver.execute_script("arguments[0].click();", input_box)
        time.sleep(1)
        input_box.clear()
        input_box.send_keys(str(start_page))
        input_box.send_keys(Keys.ENTER)
        print(f"🔁 跳转至第 {start_page} 页")
        time.sleep(5)
except Exception as e:
    print("❌ 跳转页失败：", e)
    driver.quit()
    exit()

# ==== 抓取循环 ====
all_data = []
actual_pages = 0
prev_first_title = None

try:
    for page in range(start_page, start_page + num_pages):
        print(f"📄 抓取第 {page} 页...")
        time.sleep(2)

        elements = driver.find_elements(By.XPATH, "//a[starts-with(@href, '#/GenealogySummary:')]")
        if not elements:
            print("⚠️ 当前页无数据，停止")
            break

        # 判断重复页
        spans = elements[0].find_elements(By.TAG_NAME, "span")
        if not spans:
            print("⚠️ 当前页无有效标题，终止")
            break
        current_first_title = spans[0].get_attribute("innerText").strip()
        if current_first_title == prev_first_title:
            print("⚠️ 当前页数据与上一页重复，终止")
            break
        prev_first_title = current_first_title

        # 提取数据
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

        actual_pages += 1

        # 点击“下一页”
        try:
            next_button = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//span[contains(text(), '下一页')]"))
            )
            driver.execute_script("arguments[0].click();", next_button)
        except Exception as e:
            print("❌ 翻页失败，终止：", e)
            break

except Exception as e:
    print("❌ 抓取过程中断：", e)

# ==== 保存数据 ====
end_page = start_page + actual_pages - 1
df = pd.DataFrame(all_data)
filename = f"家谱_第{start_page}页起_至第{end_page}页.csv"
df.to_csv(filename, index=False, encoding="utf-8-sig")
print(f"✅ 完成：共提取 {len(df)} 条记录，保存为：{filename}")

driver.quit()

