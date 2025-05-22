import requests
from bs4 import BeautifulSoup
import pandas as pd
header = {
    'Referer': 'https://www.jiapudata.com/iskl/mulu/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}
geneologies_info = {'name': [], 'information': []}
for page in range(0,11):
    url13 = f"https://www.jiapudata.com/jiapu/13/index_{page}.html"
    response = requests.get(url13, headers=header)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    result = soup.find_all(name='div', class_='newslist')
    for div in result:
        name_list = div.find_all(name='dt')
        for name in name_list:
            cleaned_name = name.text.strip()
            geneologies_info['name'].append(cleaned_name)
            print(cleaned_name)
        information_list = div.find_all(name='dd')
        for information in information_list:
            cleaned_information = information.text.strip()  # 去除多余的空白
            geneologies_info['information'].append(cleaned_information)  # 添加到字典
            print(cleaned_information)
    data = pd.DataFrame(geneologies_info['name'])
    data.to_excel('./1.xlsx', index=False)
    data = pd.DataFrame(geneologies_info['information'])
    data.to_excel('./2.xlsx', index=False)