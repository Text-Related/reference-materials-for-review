# -*- coding: utf-8 -*-
#循环中断--continue
#统计及格分数的平均分

score = [76,83,95,58,66,89,45,67,86,85,77,87,68]

sum = 0.0
n = 0

for single_score in score:
	if (single_score < 60):
		continue
	sum = sum + single_score
	n = n + 1
print("平均成绩为：{0}".format(sum/n))

