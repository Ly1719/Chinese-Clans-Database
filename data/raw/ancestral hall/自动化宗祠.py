import requests
import time
import csv

API_KEY = "TmDv1RSYmEgzgaKm5R50Hg3CCS5zdyUe"
output_format = "json"

# 定义关键词列表和地区列表
keywords = ["祠堂", "宗祠"]
regions = ['苍南县']

# API URL 模板
url_template = (
    f"http://api.map.baidu.com/place/v2/search?query={{}}&region={{}}"
    f"&output={output_format}&ak={API_KEY}&page_size=20&page_num={{}}"
)

def get_address(lat, lng):
    """使用逆地理编码 API 补全省、市、区地址信息"""
    geocode_url = f"http://api.map.baidu.com/reverse_geocoding/v3/?ak={API_KEY}&output=json&location={lat},{lng}"
    response = requests.get(geocode_url)
    data = response.json()

    if data.get("status") == 0:
        result = data.get("result", {})
        province = result.get("addressComponent", {}).get("province", "未知省份")
        city = result.get("addressComponent", {}).get("city", "未知城市")
        district = result.get("addressComponent", {}).get("district", "未知区县")
        return province, city, district
    else:
        return "未知省份", "未知城市", "未知区县"

def get_temple_data_for_keyword_and_region(keyword, region):
    """获取单个关键词和地区的祠堂数据"""
    all_data = []
    page_num = 0
    while True:
        url = url_template.format(keyword, region, page_num)
        response = requests.get(url)
        data = response.json()

        if data.get("status") != 0:
            print(f"[{region}] 请求失败，错误码: {data.get('status')}, 错误信息: {data.get('message')}")
            break

        results = data.get("results", [])
        if not results:
            break

        for item in results:
            name = item.get("name", "无名称")
            location = item.get("location")
            if location:
                lat = location.get("lat", "无纬度信息")
                lng = location.get("lng", "无经度信息")
                province, city, district = get_address(lat, lng)
            else:
                lat, lng = "无纬度信息", "无经度信息"
                province, city, district = "未知省份", "未知城市", "未知区县"

            address = item.get("address", "未知地址")
            all_data.append([keyword, name, lat, lng, address, province, city, district])

        page_num += 1
        time.sleep(1)

    return all_data

def save_to_csv(data, filename="苍南县.csv"):
    headers = ["关键词", "名称", "纬度", "经度", "地址", "省份", "城市", "区县"]
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)
    print(f"数据已保存到 {filename}")

if __name__ == "__main__":
    print("开始爬取祠堂分布数据...")
    all_data = []
    for keyword in keywords:  # 遍历每个关键词
        for region in regions:  # 遍历每个地区
            print(f"正在爬取关键词: {keyword}，地区: {region}")
            region_data = get_temple_data_for_keyword_and_region(keyword, region)
            all_data.extend(region_data)  # 合并数据

    save_to_csv(all_data)
    print("爬取完成！")
