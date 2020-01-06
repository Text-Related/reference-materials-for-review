#2016.12.013 今日刷题，冒泡法排序
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
			data[j],data[j+1] = data[j+1],data[j]

print('After sorted.....')
print(data)

# # 函数方式
# import random
# def bubble_sort(data):
# 	for i in range(len(data)-1):
# 		for j in range(len(data)-1):
# 			if (data[j] > data[j+1]):
# 				data[j],data[j+1] = data[j+1],data[j]
# 	return data

# data1 = []
# for n in range(20):
# 	data1.append(random.randint(1,200))

# print('Original data....')
# print(data1)

# print('After sorted.....')
# data2 = bubble_sort(data1)
# print(data2)


# # 类方式
# import random

# class SortData():
# 	def __init__(self,data):
# 		self.data = data

# 	def sort_data(self):
# 		for i in range(len(self.data)-1):   
# 			for j in range(len(self.data)-1): 
# 				if (self.data[j] > self.data[j+1]):
# 					self.data[j],self.data[j+1] = self.data[j+1],self.data[j]
# 		return self.data

# data1 = []
# for n in range(20):
# 	data1.append(random.randint(1,200))
# print('Original data....')
# print(data1)

# data2 = SortData(data1)
# data2.sort_data()

# print('After sorted.....')
# print(data2.data)
