# -*- coding: utf-8 -*-
#计算近似值

import math

i = 1; e =1; t = 1

while(1.0/t >= math.pow(10,-6)):
	t = t*i
	e = e + 1.0/t
	i = i + 1
	print("e = {0}".format(e))
	
