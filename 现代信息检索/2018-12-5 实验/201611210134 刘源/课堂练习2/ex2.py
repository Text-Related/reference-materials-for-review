#!/usr/bin/python3
# -*- coding:UTF-8 -*-

import urllib.request
import re
import os
# 定义绝对路径
localDir = 'F:\\现代信息检索\\2018-12-5 实验\\课堂练习2'
# 利用urllib.request库来提取整个网页源码
def get_one_page(url):
	headers = {
		'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
	}
	response = urllib.request.urlopen(url)
	return response.read()
# 利用正则解析出现的图片
def image_one_page(html):
	return set(re.findall(r"(images/[^\s]*?(jpg|png|gif))", str(html)))
# 利用正则解析出现的网站
def html_one_page(html):
	return set(re.findall(r"(href=[^\s]*?(html|pdf))", str(html)))
# 处理图片
def image(items):
	for item in items:
		newdir = localDir
		imagelists = item[0].split('/')
		for imagelist in imagelists:
			newdir = newdir + '\\' + imagelist
			if os.path.exists(newdir):
				continue
			else:
				os.mkdir(newdir)
			if '.' in imagelist:
				urllib.request.urlretrieve('http://history.bnu.edu.cn/' + str(item[0]), newdir)
				break
# 处理文件
def file(htmls):
	for htm in htmls:
		string = htm[0][6:]
		if 'http' in string:
			string = string[26:]
		wordlists = string.split('/')
		newdir = localDir
		for wordlist in wordlists:
			newdir = newdir + '\\' + wordlist
			if '.' in wordlist:
				urllib.request.urlretrieve('http://history.bnu.edu.cn/' + string, newdir)
				break
			if os.path.exists(newdir):
				continue
			else:
				os.mkdir(newdir)
if __name__ == "__main__":
	response = get_one_page('http://history.bnu.edu.cn/')
	items = image_one_page(response)
	htmls = html_one_page(response)
	# 先处理图片
	image(items)
	# 再处理网站文件夹
	file(htmls)