import random
def bubble_sort(data):
	lenth = len(data)
	for i in range(len(data)-1):
		for j in range(len(data)-1):
			if (data[j] > data[j+1]):
				tem = data[j]
				data[j] = data[j+1]
				data[j+1] = tem

data = []
for n in range(20):
	data.append(random.randint(1,200))
print(data)
bubble_sort(data)
print(data)
