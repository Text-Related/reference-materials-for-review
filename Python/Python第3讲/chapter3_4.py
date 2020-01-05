# -*- coding: utf-8 -*-
#计算分段函数
import math

#x=1 ;
x=int(input("请输入x值："))
if (x >= 0):
	y = math.sin(x) + 2*math.sqrt(x + math.exp(4)) - math.pow(x+1,3)
else:
	y = math.log(-5*x) - math.fabs(x*x-8*x)/(7*x) + math.e

print(y)


