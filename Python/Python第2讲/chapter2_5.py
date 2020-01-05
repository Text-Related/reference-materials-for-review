# -*- coding: utf-8 -*-
#从文件读入方式
def computing_cost(money,year):
	return  money * year *12

file_read = open('Total_fee.txt','r')
lines = file_read.readlines() 

Total_cost = 0
for line in lines:
	a = line.split()
	Total_cost = Total_money + computing_cost(int(a[0]),int(a[1]))

print(Total_cost)

file_read.close()

