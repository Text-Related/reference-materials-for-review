# -*- coding: utf-8 -*-
"""声明和调用函数getValue(salary,rate,n)，根据基本工资salary，年增长率rate,
   年数n，计算最终收入value"""
def getValue(salary,rate,i):
	value = 12 * salary * (1+rate) **i
	return value 

salary = 8000; rate = 0.1; n = 10
total = 0
for i in range(n):
	total = total + getValue(salary,rate,i)
print(total)

