#!/usr/bin/python3
# -*- coding:UTF-8 -*-

import matplotlib.pyplot as plt
import math
import random

# 定义KN近邻函数
def knn(xi):
    # 生成图像横坐标
    f = [0] * 1000
    cnt = -2
    for i in range(1000):
        f[i] = cnt
        cnt += 0.004
    # 初始化概率密度值
    p = [0] * 1000
    # 获取样本长度
    N = len(xi)
    kn = math.ceil(math.sqrt(N))
    y = [0] * N
    for i in range(1000):
        for j in range(N):
            y[j] = abs(abs(f[i]) - xi[j])
        y.sort()
        V = y[kn]
        p[i] = (kn / N) / V
    plt.plot(f, p)
    plt.show()
# 定义样本密度函数
def P(x):
    if 0.5 < x and x < 1.5:
        return 0.5
    elif 1.5 < x and x < 2.5:
        return -0.5
    else:
        return 0

s = [0] * 1024
for i in range(1024):
    x = random.uniform(0, 1)
    s[i] = P(x)

knn(s)
