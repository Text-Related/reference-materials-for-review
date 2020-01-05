#!/usr/bin/python3
# -*- coding:UTF-8 -*-

import urllib.request
from bs4 import BeautifulSoup
import json
import os
import jieba
import copy
import math
import wordcloud
# 定义绝对路径
localDir = 'F:\\现代信息检索\\2018-12-12 实验'
# 获取BeautifulSoup对象
def BS(url):
	response = urllib.request.urlopen(url)
	return BeautifulSoup(response, 'lxml')
# 建立导航字典
navigatezx = ['ttgz','bsrw','zhxw','mdwy','ztxw','jjxy','xzdt']
navigatesj = ['gysd','szzt','spkj']
navigatept = ['mtsd','xfzx','xnbk']
# 写入文件
def write_to_json(content, name):
	try:
		with open(name + '.txt', 'a', encoding = 'utf-8') as f:
			f.write(json.dumps(content, ensure_ascii = False,) + '\n')
	except Exception as e:
		print(e)
# 建立倒排索引集合
dic = {}
# 每个文件的词的计数
dic_num = {}
# 每个文件中的所有词的词频
dic_text_frequency = {}
# 存放dic_text_frequency
dic_text_all = {}
# 每个文档的词数
dic_text = {}
# IDF
dic_idf = {}
# TF_IDF值
dic_tf_idf = {}
# 赋值初始网页
set_this_text = set()
#记录当前文章的词
url = 'http://news.bnu.edu.cn'
# 定义文档数
text_num = 0
# 主程序入口
text_string = ''
if __name__ == "__main__":
	num = ''
	# 头条关注
	header = url + '/zx/' + navigatezx[0]
	newdir = localDir + '\\zx\\' + navigatezx[0]
	if os.path.exists(newdir):
		pass
	else:
		os.makedirs(newdir)
	for i in range(24):
		index = '/index' + num + '.htm'
		text = header + index
		soup = BS(text)
		for link in soup.find_all(name = 'li', class_ = 'item-info01'):
			soupnew = BeautifulSoup(str(link), 'lxml')
			href = soupnew.find('a').get('href')
			if 'http' not in href:
				urllib.request.urlretrieve(header + '/' + href, newdir + '\\' + href)
				Soup = BS(header + '/' + href)
				for content in Soup.find_all(name = 'div', class_ = 'article'):
					text_num += 1
					text_string += content.get_text()
					write_to_json(content.get_text(), 'zx/ttgz/' + href[:-4])
					result = jieba.tokenize(content.get_text())
					for token in result:
						if href[:-4] in dic_text:
							dic_text[href[:-4]] += 1
						else:
							dic_text[href[:-4]] = 1 
						if token[0] not in dic:
							dic[token[0]] = set()
						if token[0] not in set_this_text:
							set_this_text.add(token[0])
							dic_num[token[0]] = 0
						dic[token[0]].add(href[:-4])
						dic_num[token[0]] += 1
					for cc in dic_num:
						dic_text_frequency[cc] = dic_num[cc] / dic_text[href[:-4]]
					dic_text_all[href[:-4]] = copy.deepcopy(dic_text_frequency)
					dic_text_frequency = {}
					dic_text = {}
					set_this_text = set()
					dic_num = {}
		print(i)
		num = str(i + 1)
	num = ''
	# 师大人物
	header = url + '/zx/' + navigatezx[1]
	newdir = localDir + '\\zx\\' + navigatezx[1]
	if os.path.exists(newdir):
		pass
	else:
		os.makedirs(newdir)
	for i in range(6):
		index = '/index' + num + '.htm'
		text = header + index
		soup = BS(text)
		for link in soup.find_all(name = 'li', class_ = 'item-info01'):
			soupnew = BeautifulSoup(str(link), 'lxml')
			href = soupnew.find('a').get('href')
			if 'http' not in href:
				urllib.request.urlretrieve(header + '/' + href, newdir + '\\' + href)
				Soup = BS(header + '/' + href)
				for content in Soup.find_all(name = 'div', class_ = 'article'):
					text_num += 1
					text_string += content.get_text()
					write_to_json(content.get_text(), 'zx/bsrw/' + href[:-4])
					result = jieba.tokenize(content.get_text())
					for token in result:
						if token[0] != '\n':
							if href[:-4] in dic_text:
								dic_text[href[:-4]] += 1
							else:
								dic_text[href[:-4]] = 1 
							if token[0] not in dic:
								dic[token[0]] = set()
							if token[0] not in set_this_text:
								set_this_text.add(token[0])
								dic_num[token[0]] = 0
							dic[token[0]].add(href[:-4])
							dic_num[token[0]] += 1
						else:
							continue
					for cc in dic_num:
						dic_text_frequency[cc] = dic_num[cc] / dic_text[href[:-4]]
					dic_text_all[href[:-4]] = copy.deepcopy(dic_text_frequency)
					dic_text_frequency = {}
					dic_text = {}
					set_this_text = set()
					dic_num = {}
		print(' ',i)
		num = str(i + 1)
	num = ''
	# 综合新闻
	header = url + '/zx/' + navigatezx[2]
	newdir = localDir + '\\zx\\' + navigatezx[2]
	if os.path.exists(newdir):
		pass
	else:
		os.makedirs(newdir)
	for i in range(25):
		index = '/index' + num + '.htm'
		text = header + index
		soup = BS(text)
		for link in soup.select('.list01 li'):
			soupnew = BeautifulSoup(str(link), 'lxml')
			href = soupnew.find('a').get('href')
			if 'http' not in href:
				urllib.request.urlretrieve(header + '/' + href, newdir + '\\' + href)
				Soup = BS(header + '/' + href)
				for content in Soup.find_all(name = 'div', class_ = 'article'):
					text_num += 1
					text_string += content.get_text()
					write_to_json(content.get_text(), 'zx/zhxw/' + href[:-4])
					result = jieba.tokenize(content.get_text())
					for token in result:
						if token[0] != '\n':
							if href[:-4] in dic_text:
								dic_text[href[:-4]] += 1
							else:
								dic_text[href[:-4]] = 1 
							if token[0] not in dic:
								dic[token[0]] = set()
							if token[0] not in set_this_text:
								set_this_text.add(token[0])
								dic_num[token[0]] = 0
							dic[token[0]].add(href[:-4])
							dic_num[token[0]] += 1
						else:
							continue
					for cc in dic_num:
						dic_text_frequency[cc] = dic_num[cc] / dic_text[href[:-4]]
					dic_text_all[href[:-4]] = copy.deepcopy(dic_text_frequency)
					dic_text_frequency = {}
					dic_text = {}
					set_this_text = set()
					dic_num = {}
		print('  ',i)
		num = str(i + 1)
	num = ''
	# 木铎文韵
	header = url + '/zx/' + navigatezx[3]
	newdir = localDir + '\\zx\\' + navigatezx[3]
	if os.path.exists(newdir):
		pass
	else:
		os.makedirs(newdir)
	for i in range(1):
		index = '/index' + num + '.htm'
		text = header + index
		soup = BS(text)
		for link in soup.select('.list01 li'):
			soupnew = BeautifulSoup(str(link), 'lxml')
			href = soupnew.find('a').get('href')
			if 'http' not in href:
				urllib.request.urlretrieve(header + '/' + href, newdir + '\\' + href)
				Soup = BS(header + '/' + href)
				for content in Soup.find_all(name = 'div', class_ = 'article'):
					text_num += 1
					text_string += content.get_text()
					write_to_json(content.get_text(), 'zx/mdwy/' + href[:-4])
					result = jieba.tokenize(content.get_text())
					for token in result:
						if token[0] != '\n':
							if href[:-4] in dic_text:
								dic_text[href[:-4]] += 1
							else:
								dic_text[href[:-4]] = 1 
							if token[0] not in dic:
								dic[token[0]] = set()
							if token[0] not in set_this_text:
								set_this_text.add(token[0])
								dic_num[token[0]] = 0
							dic[token[0]].add(href[:-4])
							dic_num[token[0]] += 1
						else:
							continue
					for cc in dic_num:
						dic_text_frequency[cc] = dic_num[cc] / dic_text[href[:-4]]
					dic_text_all[href[:-4]] = copy.deepcopy(dic_text_frequency)
					dic_text_frequency = {}
					dic_text = {}
					set_this_text = set()
					dic_num = {}
		print('   ',i)
		num = str(i + 1)
	num = ''
	# 菁菁新闻
	header = url + '/zx/' + navigatezx[5]
	newdir = localDir + '\\zx\\' + navigatezx[5]
	if os.path.exists(newdir):
		pass
	else:
		os.makedirs(newdir)
	for i in range(1):
		index = '/index' + num + '.htm'
		text = header + index
		soup = BS(text)
		for link in soup.select('.list01 li'):
			soupnew = BeautifulSoup(str(link), 'lxml')
			href = soupnew.find('a').get('href')
			if 'http' not in href:
				urllib.request.urlretrieve(header + '/' + href, newdir + '\\' + href)
				Soup = BS(header + '/' + href)
				for content in Soup.find_all(name = 'div', class_ = 'article'):
					text_num += 1
					text_string += content.get_text()
					write_to_json(content.get_text(), 'zx/jjxy/' + href[:-4])
					result = jieba.tokenize(content.get_text())
					for token in result:
						if token[0] != '\n':
							if href[:-4] in dic_text:
								dic_text[href[:-4]] += 1
							else:
								dic_text[href[:-4]] = 1 
							if token[0] not in dic:
								dic[token[0]] = set()
							if token[0] not in set_this_text:
								set_this_text.add(token[0])
								dic_num[token[0]] = 0
							dic[token[0]].add(href[:-4])
							dic_num[token[0]] += 1
						else:
							continue
					for cc in dic_num:
						dic_text_frequency[cc] = dic_num[cc] / dic_text[href[:-4]]
					dic_text_all[href[:-4]] = copy.deepcopy(dic_text_frequency)
					dic_text_frequency = {}
					dic_text = {}
					set_this_text = set()
					dic_num = {}
		print('    ',i)
		num = str(i + 1)
	num = ''
	# 学术动态
	header = url + '/zx/' + navigatezx[6]
	newdir = localDir + '\\zx\\' + navigatezx[6]
	if os.path.exists(newdir):
		pass
	else:
		os.makedirs(newdir)
	for i in range(19):
		index = '/index' + num + '.htm'
		text = header + index
		soup = BS(text)
		for link in soup.select('.list01 li'):
			soupnew = BeautifulSoup(str(link), 'lxml')
			href = soupnew.find('a').get('href')
			if 'http' not in href:
				urllib.request.urlretrieve(header + '/' + href, newdir + '\\' + href)
				Soup = BS(header + '/' + href)
				for content in Soup.find_all(name = 'div', class_ = 'article'):
					text_num += 1
					text_string += content.get_text()
					write_to_json(content.get_text(), 'zx/xzdt/' + href[:-4])
					result = jieba.tokenize(content.get_text())
					for token in result:
						if token[0] != '\n':
							if href[:-4] in dic_text:
								dic_text[href[:-4]] += 1
							else:
								dic_text[href[:-4]] = 1 
							if token[0] not in dic:
								dic[token[0]] = set()
							if token[0] not in set_this_text:
								set_this_text.add(token[0])
								dic_num[token[0]] = 0
							dic[token[0]].add(href[:-4])
							dic_num[token[0]] += 1
						else:
							continue
					for cc in dic_num:
						dic_text_frequency[cc] = dic_num[cc] / dic_text[href[:-4]]
					dic_text_all[href[:-4]] = copy.deepcopy(dic_text_frequency)
					dic_text_frequency = {}
					dic_text = {}
					set_this_text = set()
					dic_num = {}
		print('      ',i)
		num = str(i + 1)
	num = ''
	# 媒体师大
	header = url + '/pt/' + navigatept[0]
	newdir = localDir + '\\pt\\' + navigatept[0]
	if os.path.exists(newdir):
		pass
	else:
		os.makedirs(newdir)
	for i in range(5):
		index = '/index' + num + '.htm'
		text = header + index
		soup = BS(text)
		for link in soup.select('.list01 li'):
			soupnew = BeautifulSoup(str(link), 'lxml')
			href = soupnew.find('a').get('href')
			if 'http' not in href:
				urllib.request.urlretrieve(header + '/' + href, newdir + '\\' + href)
				Soup = BS(header + '/' + href)
				for content in Soup.find_all(name = 'div', class_ = 'article'):
					text_num += 1
					text_string += content.get_text()
					write_to_json(content.get_text(), 'pt/mtsd/' + href[:-4])
					result = jieba.tokenize(content.get_text())
					for token in result:
						if token[0] != '\n':
							if href[:-4] in dic_text:
								dic_text[href[:-4]] += 1
							else:
								dic_text[href[:-4]] = 1 
							if token[0] not in dic:
								dic[token[0]] = set()
							if token[0] not in set_this_text:
								set_this_text.add(token[0])
								dic_num[token[0]] = 0
							dic[token[0]].add(href[:-4])
							dic_num[token[0]] += 1
						else:
							continue
					for cc in dic_num:
						dic_text_frequency[cc] = dic_num[cc] / dic_text[href[:-4]]
					dic_text_all[href[:-4]] = copy.deepcopy(dic_text_frequency)
					dic_text_frequency = {}
					dic_text = {}
					set_this_text = set()
					dic_num = {}
		print('       ',i)
		num = str(i + 1)
	print('checkpoint1')
	for i in dic:
		dic_idf[i] = math.log(text_num / (len(dic[i]) + 1))
	print('checkpoint2')
	for j in dic_text_all:
		tf_idf = 0
		for k in dic_text_all[j]:
			dic_text_all[j][k] = dic_text_all[j][k] * dic_idf[k]
			tf_idf += dic_text_all[j][k]
		dic_tf_idf[j] = tf_idf
	print('checkpoint3')
	print(dic)
	print(sorted(dic_tf_idf.items(), key=lambda e:e[1],reverse = True))

	#词云
	cut = jieba.cut(text_string)
	string = ' '.join(cut)
	font = r'C:\Windows\Fonts\FZSTK.TTF'
	wc = wordcloud.WordCloud(font_path=font,background_color='white',width=1000,height=800,).generate(string)
	wc.to_file(localDir+'\\result.png')
	print("end")