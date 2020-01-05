# -*- coding: utf-8 -*-
#循环中断--continue
#从excel表格中读数据，统计及格分数的平均分
# 需下载xlrd库

import xlrd

xls = xlrd.open_workbook("score.xlsx")

sheet = xls.sheets()[0]   #从第几个表格中取数据
col = sheet.col_values(2) #获取第几列数据

sum = 0.0
n = 0

for single_score in col:
	if (single_score < 60):
		continue
	sum = sum + single_score
	n = n + 1
print("平均成绩为：{0}".format(sum/n))

