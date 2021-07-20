#!/usr/bin/python
# -*- coding: UTF-8 -*-

import http.client
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
host = "qyapi.weixin.qq.com"
key = "b6837ee3-59f5-40b0-8a78-56954ada1a4f"
url = "/cgi-bin/webhook/send?key={key}".format(key=key)
header = {
    "Content-Type": "application/json"
}
data = json.dumps(markdown)
httpConn = http.client.HTTPSConnection(host=host, port=443, timeout=60)
httpConn.request("POST", url=url, body=data, headers=header)
response = httpConn.getresponse()
print(response.read().decode())
# {"errcode":0,"errmsg":"ok"}
