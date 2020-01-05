# !/usr/bin/python3
# -*- coding:UTF-8 -*-

import matplotlib.pyplot as plt
import math
import random

p = [0] * 1000
f = [0] * 1000
cnt = -5
for i in range(1000):
	f[i] = cnt
	cnt += 0.01
# h:窗口长度，N:采样点数，x:样本数据，f代表横坐标范数，核函数为高斯函数
def GaussParzen(x, h, N):
	b = 0
	h1 =  h / math.sqrt(N)
	for i in range(0, 1000):
		for j in range(0, N):
			b = b + math.exp(((f[i]-x[j]) / h1) ** 2 / (-2)) / math.sqrt(2 * math.pi) / h1
		p[i] =  b / N
		b = 0
# 核函数为方窗函数
def SquareParzen(x, h, N):
	b = 0
	h1 =  h / math.sqrt(N)
	for i in range(0, 1000):
		for j in range(0, N):
			if abs((x[j] - f[i]) / h) <= 1/2:
				q = 1 / h
			else:
				q = 0
			b = b + q
		p[i] =  b / N
		b = 0
# 定义样本密度函数
def P(x):
	if -2.5 < x and x < -2:
		return 1
	elif 2.5 < x and x < 3:
		return 0.5
	else:
		return 0

s = [0] * 10000
for i in range(10000):
	x = random.uniform(-5, 5)
	s[i] = P(x)
# GaussParzen(s, 0.05, 100)
SquareParzen(s, 0.1, 10)
plt.plot(f, p)
plt.show()