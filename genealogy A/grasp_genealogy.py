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

# ==== 设置参数 ====
CHROMEDRIVER_PATH = r"C:\Users\user\Desktop\thesis_data\code\chromedriver-win64\chromedriver.exe"
start_page = 4103
num_pages = 100  # 最大抓取页数（程序会在翻页失败或数据重复时提前停止）

# ==== 初始化浏览器 ====
options = Options()
# options.add_argument("--headless")  # 可取消注释隐藏浏览器界面
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://jiapu.library.sh.cn/#/genealogyCenter")
print("✅ 成功打开网页")
time.sleep(5)

# ==== 点击“确定” ====
try:
    confirm_span = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[text()='确定']"))
    )
    ActionChains(driver).move_to_element(confirm_span).click().perform()
    print("✅ 点击‘确定’成功")
except Exception as e:
    print("❌ 点击失败：", e)
    driver.quit()
    exit()

WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "//a[starts-with(@href, '#/GenealogySummary:')]"))
)

# ==== 跳页（若非第一页）====
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
        print(f"🔁 跳转至第 {start_page} 页")
        time.sleep(5)
    except Exception as e:
        print("❌ 跳页失败：", e)
        driver.quit()
        exit()

# ==== 抓取循环 ====
all_data = []
prev_first_title = None
actual_pages = 0

try:
    for page in range(start_page, start_page + num_pages):
        print(f"📄 正在抓取第 {page} 页...")
        time.sleep(2)

        elements = driver.find_elements(By.XPATH, "//a[starts-with(@href, '#/GenealogySummary:')]")
        if not elements:
            print("⚠️ 当前页无家谱卡片，停止抓取")
            break

        # 防重复判断
        spans = elements[0].find_elements(By.TAG_NAME, "span")
        if not spans:
            print("⚠️ 当前页首条家谱无标题，终止")
            break

        current_first_title = spans[0].get_attribute("innerText").strip()
        if current_first_title == prev_first_title:
            print(f"⚠️ 第 {page} 页与上一页重复，终止抓取")
            break
        prev_first_title = current_first_title

        # 抓取当前页数据
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
            print("❌ 翻页失败，程序终止：", e)
            break

except Exception as e:
    print("❌ 程序中断：", e)

# ==== 保存数据 ====
df = pd.DataFrame(all_data)
end_page = start_page + actual_pages - 1
filename = f"家谱_第{start_page}页起_至第{end_page}页.csv"
df.to_csv(filename, index=False, encoding="utf-8-sig")
print(f"✅ 共抓取 {actual_pages} 页（第 {start_page}~{end_page} 页），共 {len(df)} 条记录，已保存为：{filename}")

driver.quit()