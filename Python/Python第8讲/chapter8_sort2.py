# coding:utf-8
# 函数方式
import random
def bubble_sort(data):
	lenth = len(data)
	for j in range(len(data)-1):
			if (data[j] > data[j+1]):
				tem = data[j]
				data[j] = data[j+1]
				data[j+1] = tem

data = []
for n in range(20):
	data.append(random.randint(1,200))

print('Original data....')
print(data)

print('After sorted.....')
bubble_sort(data)
print(data)

