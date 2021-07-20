#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import urllib.request
import os


def get_sougou_image(query, tagQSign, size, pages, path):
    url = "https://pic.sogou.com/napi/pc/searchList"
    params = {
        "query": query,
        "tagQSign": tagQSign,
        "start": 0,
        "xml_len": size,
        "cwidth": 1920,
        "cheight": 1080,
        "mode": 13,
        "dm": 4
    }
    # 文件目录不存在时，新建目录
    path += "/" + query + "/" + tagQSign.split(",")[0] + "/"
    if not os.path.exists(path):
        os.makedirs(path)
    m = 1
    for page in range(0, pages):
        params["start"] = page * size
        print('***** 第' + str(page + 1) + '页 *****' + '   Downloading...')
        response = requests.get(url, params=params)
        data = response.json()
        images = data["data"]["items"]
        for image in images:
            image_url = image["oriPicUrl"]
            print('***** ' + image_url + ' *****')
            print('***** ' + str(m) + ' *****' + '  Downloading...')
            try:
                urllib.request.urlretrieve(image_url, path + str(m) + '.jpg')
            except Exception:
                print('***** ' + str(m) + ' *****' + '  Downloading Fail')
            m += 1
        # 一页图片数不够分页大小时，表示没有下一页了，退出循环
        if len(images) < size:
            break


get_sougou_image("壁纸", "美女,fa976caa", 48, 2, "G:/Download")

