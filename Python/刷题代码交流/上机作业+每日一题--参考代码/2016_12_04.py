#2016.12.04 今日一题:  求1000000以内的所有素数
import math
import time

start = time.clock()
lst = [2]
for i in range(3,10000,2):
	m = int(math.sqrt(i))
	for j in range(2,m+2):
		if i%j == 0:
			break
	if j == m+1:
		lst.append(i)
end = time.clock()
print('the processing time is:',end-start)

for i in range(20):
	print(lst[i],end = ' ')


