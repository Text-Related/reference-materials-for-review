# -*- coding: utf-8 -*-
#计算分段函数
import math

def compute_fun1(x):
	if (x >= 0):
		y = math.sin(x) + 2*math.sqrt(x + math.exp(4)) - math.pow(x+1,3)
	else:
		y = math.log(-5*x) - math.fabs(x*x-8*x)/(7*x) + math.e
	return y

print(compute_fun1(1))


