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

# === 基本设置 ===
CHROMEDRIVER_PATH = r"C:\Users\m1780\Desktop\Thesis\data of clans\code\chromedriver-win64\chromedriver.exe"
start_page = 1     # 起始页码
num_pages = 100     # 要抓多少页（从 start_page 开始）
FILTER_SURNAME = ""     # 姓氏关键词，如只抓顾姓（留空 "" 表示不过滤）
FILTER_YEAR = ""       # 撰修时间关键词，如“清”或“1980”（留空表示不过滤）
FILTER_REGION = ""    # 地区关键词，从谱名中匹配（留空表示不过滤）

# === 启动浏览器 ===
options = Options()
# options.add_argument("--headless")  # 调试建议注释掉
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://jiapu.library.sh.cn/#/genealogyCenter")
print("✅ 成功打开网页，等待加载...")
time.sleep(5)

# === 点击“确定”按钮 ===
try:
    confirm_span = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[text()='确定']"))
    )
    ActionChains(driver).move_to_element(confirm_span).click().perform()
    print("✅ 已点击‘确定’，等待数据加载...")
except Exception as e:
    print("❌ 点击失败：", e)
    driver.quit()
    exit()

# === 等待第一页加载 ===
try:
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//a[starts-with(@href, '#/GenealogySummary:')]"))
    )
except Exception as e:
    print("❌ 家谱列表加载失败：", e)
    driver.save_screenshot("load_failed.png")
    with open("page_source_debug.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    driver.quit()
    exit()

# === 跳页（非第一页）===
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
        print("❌ 跳页失败：", e)
        driver.quit()
        exit()

# === 开始翻页抓取 ===
all_data = []
try:
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

            title = safe_text(spans[0])
            editor = safe_text(spans[1])
            surname = safe_text(spans[2])
            year = safe_text(spans[3])
            hall = safe_text(spans[4])
            summary = safe_text(spans[5])
            link = "https://jiapu.library.sh.cn/" + el.get_attribute("href").lstrip("#/")

            # === 筛选逻辑 ===
            if FILTER_SURNAME and FILTER_SURNAME not in surname:
                continue
            if FILTER_YEAR and FILTER_YEAR not in year:
                continue
            if FILTER_REGION and FILTER_REGION not in title:
                continue

            all_data.append({
                "谱名": title,
                "责任者": editor,
                "姓氏": surname,
                "撰修时间": year,
                "堂号": hall,
                "家谱简介": summary,
                "详情链接": link
            })

        # === 点击下一页 ===
        if page < start_page + num_pages - 1:
            try:
                next_button = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//span[contains(text(), '下一页')]"))
                )
                driver.execute_script("arguments[0].click();", next_button)
            except Exception as e:
                raise RuntimeError(f"⚠️ 翻页失败：{e}")

except Exception as e:
    print("❌ 程序中断：", e)
    df = pd.DataFrame(all_data)
    df.to_csv(f"家谱_第{start_page}_页起_中断保存.csv", index=False, encoding="utf-8-sig")
    print(f"⚠️ 已保存中断前 {len(df)} 条记录")
    driver.quit()
    exit()

# === 正常保存结果 ===
df = pd.DataFrame(all_data)
df.to_csv(f"家谱_第{start_page}_页起_共{num_pages}页.csv", index=False, encoding="utf-8-sig")
print(f"✅ 抓取完成，共提取 {len(df)} 条记录，已保存为 CSV")

driver.quit()
