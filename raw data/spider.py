# # 抓取电影封面图
import requests
from bs4 import BeautifulSoup
#
# header = {'Referer':'https://ssr1.scrape.center/','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}
#
# response = requests.get("https://p1.meituan.net/movie/6bea9af4524dfbd0b668eaa7e187c3df767253.jpg@464w_644h_1e_1c", headers=header)
# print(response.content)
# with open("movie.jpg", "wb") as f:
#     f.write(response.content)

#抓取页面数据

header = {'Referer':'https://scrape.center/',
          'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}

response = requests.get("https://ssr1.scrape.center/", headers=header)
# print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
result = soup.find_all(name='div', class_='p-h el-col el-col-24 el-col-xs-9 el-col-sm-13 el-col-md-16')
for i in range(len(result)):

    # print(result)
    print(result[i].h2.string)
    button_list=result[i].find_all(name='button',class_='el-button category el-button--primary el-button--mini')
    # print(len(button_list))
    for button in button_list:
        print(button.span.string)

    info_list = result[i].find_all(name='div',class_='m-v-sm info')
    # print(info_list)
    for info in info_list:
        span_list = info.find_all(name='span')
        for s in span_list:
            if s.string != ' / ':
                print(s.string)

    score = soup.find_all(name='p',class_='score m-t-md m-b-n-sm')
    print(score[i].string.strip())
    print('--------------')

#抓取页面数据
header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}
response = requests.get('https://www.jiapudata.com/iskl/mulu/',)
print(response.text)








#抓取整站的电影信息
#将数据导入excel


