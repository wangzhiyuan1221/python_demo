#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import mysql.connector
import json

config = {
    'host': '10.242.142.107',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'database': 'test'
}

conn = mysql.connector.connect(**config)
cursor = conn.cursor()
sql = "select ddate date, item, num, money from test limit 1"
cursor.execute(sql)
resultStr = "date: {date}, item: {item}, num: {num}, money: {money}"
result = ""
for (date, item, num, money) in cursor:
    result += resultStr.format(date=date, item=item, num=num, money=money)
cursor.close()
conn.close()
markdown = {
    "msgtype": "markdown",
    "markdown": {
        "content": result
    }
}
key = "b6837ee3-59f5-40b0-8a78-56954ada1a4f"
url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={key}".format(key=key)
response = requests.post(url, json=markdown)
# response.raise_for_status()
print(response.text)
# {"errcode":0,"errmsg":"ok"}
if json.loads(response.text)["errcode"] == 0:
    print("发送成功")
else:
    print("发送失败")

