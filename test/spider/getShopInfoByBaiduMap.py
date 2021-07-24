#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import time


def get_shop_info(region, query, tag, size, filePath):
    url = "http://api.map.baidu.com/place/v2/search"
    params = {
        "ak": "your ak",
        "query": query,
        "tag": tag,
        "page_num": 0,
        "page_size": size,
        "output": "json",
        "region": region
    }

    response = requests.get(url, params=params)
    data = response.json()
    total = data["total"]
    pages = total // size
    if total % size != 0:
        pages += 1
    results = data["results"]
    with open(filePath, "a") as file:
        for result in results:
            file.write(result["name"])
            file.write("  " + result.get("telephone", "没有电话"))
            file.write("  " + result["province"] + result["city"] + result["area"])
            file.write("  " + result["address"] + "\n")
        print("第1页完成")
        time.sleep(1)
        for page in range(1, pages):
            params["page_num"] = page
            response = requests.get(url, params=params)
            data = response.json()
            results = data["results"]
            for result in results:
                file.write(result["name"])
                file.write("  " + result.get("telephone", "没有电话"))
                file.write("  " + result["province"] + result["city"] + result["area"])
                file.write("  " + result["address"] + "\n")
            print("第" + str(page + 1) + "页完成")
            time.sleep(1)


def get_city_shop_info():
    city_list = ["深圳市", "广州市", "北京市"]
    for city in city_list:
        print(city + "开始")
        get_shop_info(city, "家具建材", "卖场,市场", 20, "F:/ddd.txt")
        print(city + "结束")


get_city_shop_info()

