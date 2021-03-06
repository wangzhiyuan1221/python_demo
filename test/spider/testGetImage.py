#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import urllib.request
import os


def get_sougou_image(category, tag, size, pages, path):
    url = "https://pic.sogou.com/pics/channel/getAllRecomPicByTag.jsp"
    params = {
        "category": category,
        "tag": tag,
        "start": 0,
        "len": size,
        "width": 1920,
        "height": 1080
    }
    m = 1
    # 文件目录不存在时，新建目录
    path += "/" + category + "/" + tag + "/"
    if not os.path.exists(path):
        os.makedirs(path)
    for page in range(0, pages):
        params["start"] = page * size
        print('***** 第' + str(page + 1) + '页 *****' + '   Downloading...')
        response = requests.get(url, params=params)
        data = response.json()
        images = data["all_items"]
        for image in images:
            image_url = image["pic_url"]
            print('***** ' + image_url + ' *****')
            print('***** ' + str(m) + '.jpg *****' + '  Downloading...')
            try:
                urllib.request.urlretrieve(image_url, path + str(m) + '.jpg')
            except Exception:
                print('***** ' + str(m) + ' *****' + '  Downloading Fail')
            m += 1
        # 一页图片数不够分页大小时，表示没有下一页了，退出循环
        if len(images) < size:
            break


get_sougou_image("明星", "全部", 15, 10, "G:/Download")

