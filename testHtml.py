#!/usr/bin/python
# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup

html_str = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's stopy</b></p>
<p class="story">Once upon a time there were three little sisters;and their names where
<a href="http://example.com/elsie" class="sister" id="link1"><!--Elsie--></a>
"""

soup = BeautifulSoup(html_str, 'lxml')
print(soup.a.attrs['id'])
print(soup.a.attrs['href'])
print(soup.p.attrs['class'][0])
