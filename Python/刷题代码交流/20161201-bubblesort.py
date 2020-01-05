# coding:utf-8
# 2016-12-01-冒泡法排序
import random

data = []
for n in range(20):  #随机生成20数
    data.append(random.randint(1,200))

print('Original data....')
print(data)

for i in range(len(data)-1): 
    flag = 0
    for j in range(len(data)-1):
        if (data[j] > data[j+1]): #前后两个比较，交换数据
            tem = data[j]
            data[j] = data[j+1]
            data[j+1] = tem
            flag = 1
            
    if(flag == 0):
        break;

print('After sorted.....')
print(data)
