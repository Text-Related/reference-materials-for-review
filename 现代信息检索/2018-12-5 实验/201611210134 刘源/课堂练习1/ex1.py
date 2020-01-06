#!/usr/bin/python3
# -*- coding:UTF-8 -*-

import urllib.request
import re

# 利用urllib.request库来提取整个网页源码
def get_one_page(url):
	headers = {
		'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
	}
	response = urllib.request.urlopen(url)
	return response.read()
# 利用正则解析出现的网页源码
def parse_one_page(html):
	return set(re.findall(r"(images/[^\s]*?(jpg|png|gif))", str(html)))

if __name__ == "__main__":
	tmp = 0
	response = get_one_page('http://history.bnu.edu.cn/')
	items = parse_one_page(response)
	for item in items:
		tmp += 1
		urllib.request.urlretrieve('http://history.bnu.edu.cn/' + str(item[0]), '%s.jpg'%tmp)
