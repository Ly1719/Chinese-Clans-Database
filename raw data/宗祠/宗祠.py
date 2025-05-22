import requests
import time
import csv

# 百度地图 API Key
API_KEY = "TmDv1RSYmEgzgaKm5R50Hg3CCS5zdyUe"

# 查询条件
keyword = "宗祠"
region = ("平阳县")  # 替换为目标省份或城市
output_format = "json"
url_template = (
    f"http://api.map.baidu.com/place/v2/search?query={keyword}&region={region}"
    f"&output={output_format}&ak={API_KEY}&page_size=20&page_num={{}}"
)


# 爬取祠堂分布数据
def get_temple_data():
    all_data = []
    page_num = 0
    while True:
        url = url_template.format(page_num)
        response = requests.get(url)
        data = response.json()

        if data["status"] != 0:  # 检查是否请求成功
            print(f"请求失败，错误码: {data['status']}")
            break

        results = data.get("results", [])
        if not results:  # 没有更多数据时退出
            break

        # 提取需要的信息
        for item in results:
            name = item.get("name")
            address = item.get("address", "无地址信息")
            province = item.get("province", "无省份信息")
            city = item.get("city", "无城市信息")
            district = item.get("area", "无区县信息")

            all_data.append([name, address, province, city, district])

        page_num += 1
        time.sleep(1)  # 避免触发 API 限制

    return all_data


# 保存数据到 CSV 文件
def save_to_csv(data, filename="祠堂分布数据.csv"):
    headers = ["名称", "地址", "省份", "城市", "区县"]
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)
    print(f"数据已保存到 {filename}")


# 主程序
if __name__ == "__main__":
    print("开始爬取祠堂分布数据...")
    temple_data = get_temple_data()
    save_to_csv(temple_data)
    print("爬取完成！")

