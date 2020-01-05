# coding:utf-8
# 类方式
import random

class SortData():
	def __init__(self,data):
		self.data = data

	def sort_data(self):
		for i in range(len(self.data)-1):   
			for j in range(len(self.data)-1): 
				if (self.data[j] > self.data[j+1]):
					tem = self.data[j]
					self.data[j] = self.data[j+1]
					self.data[j+1] = tem

data = []
for n in range(20):
	data.append(random.randint(1,200))
print('Original data....')
print(data)

data1 = SortData(data)
data1.sort_data()

print('After sorted.....')
print(data)