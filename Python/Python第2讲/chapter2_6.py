# -*- coding: utf-8 -*-
#文件的读写操作

def computing_cost(money,year):
	return  money * year *12

file_read = open('Total_fee.txt','r')
file_write = open('Result.txt','w')
lines = file_read.readlines() 
i = 1
Total_cost = 0
for line in lines:
	a = line.split()
	Total_cost = Total_cost + computing_cost(int(a[0]),int(a[1]))
	file_write.write("前{0}次费用和: {1} \n".format(i,Total_cost))
	i = i +1

print(Total_cost)

file_read.close()
file_write.close()

