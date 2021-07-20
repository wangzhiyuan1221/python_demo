#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json
from requests.exceptions import ReadTimeout, ConnectTimeout

# response = requests.get("https://www.baidu.com")
# print(type(response))
# print(response.status_code)
# print(type(response.text))
#
# response.encoding = "utf-8"
# print(response.text)
# print(response.cookies)
#
# print(response.content)
# print(response.content.decode("utf-8"))

# url = "http://httpbin.org/get"
# data = {
#     'name': 'Andy',
#     'age': 28
# }
# response = requests.get(url, params=data)
# print(response.url)
# print(response.text)

# print(type(response.text))
# print(response.json())
# print(json.loads(response.text))
# print(type(response.json()))
# print(response.json()['args'])
# print(type(response.json()['args']))
# print(response.json()['args']['age'])

# url = "https://www.zhihu.com"
# response = requests.get(url)
# response.encoding = "utf-8"
# print(response.text)

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                   'Chrome/57.0.2987.133 Safari/537.36'
# }
# response = requests.get(url, headers=headers)
# response.encoding = "utf-8"
# print(response.text)

url = "http://httpbin.org/post"
data = {
    'name': 'Andy',
    'age': 28
}
response = requests.post(url, data=data)
print(response.text)
response = requests.post(url, json=data)
print(response.text)

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/86.0.4240.75 Safari/537.36"
# }
# response = requests.get("https://www.jianshu.com/404.html", headers=headers)
# print(response.status_code)
# if response.status_code != requests.codes.ok:
#     print("404")
#
# response = requests.get("https://www.jianshu.com", headers=headers)
# print(response.status_code)
# if response.status_code == 200:
#     print("200")

# response = requests.get("https://www.baidu.com")
# print(response.cookies)
# response.cookies.keys()
# for key, value in response.cookies.items():
#     print(key, '==', value)
#
# for key in response.cookies.keys():
#     print(key)

# try:
#     response = requests.get("http://httpbin.org/get", timeout=0.3)
#     print(response.status_code)
# except ReadTimeout:
#     print("TimeOut")
# except ConnectTimeout:
#     print("ConnectTimeout")
# finally:
#     print("Finish")

