# -*- coding: utf-8 -*-
#循环中断--break
#计算素数：在大于1的自然数中，除了1和它本身以外不再有其他因数的数

import math

for i in range(50,100+1):
	for j in range(2,int(math.sqrt(i)) + 1):
		if i % j == 0:
			break
	else:
		print(i)
