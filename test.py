from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


# 配置路径
CHROMEDRIVER_PATH = r"C:\Users\user\Desktop\thesis_data\chromedriver-win64\chromedriver.exe"
service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service)

# 创建浏览器启动参数
options = Options()
options.add_argument("--headless")  # 可选：无头模式（不显示窗口）
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

# 初始化浏览器驱动服务
service = Service(CHROMEDRIVER_PATH)

# 启动浏览器
driver = webdriver.Chrome(service=service, options=options)

# 访问网页
driver.get("https://jiapu.library.sh.cn/#/genealogyCenter")

# 你可以加这句看看有没有打开
print("✅ 成功打开网页！")

# 最后记得关闭浏览器
driver.quit()