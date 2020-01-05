# coding:utf-8
# 传统方式
import random

data = []
for n in range(20):
	data.append(random.randint(1,200))

print('Original data....')
print(data)

for i in range(len(data)-1):
	for j in range(len(data)-1):
		if (data[j] > data[j+1]):
			tem = data[j]
			data[j] = data[j+1]
			data[j+1] = tem

print('After sorted.....')
print(data)