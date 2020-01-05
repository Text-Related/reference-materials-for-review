def my_sum4(a,b,*c,**d):
	total = a + b
	print('c 的值：',c)
	for n in c:
		total = total + n
		print('*c:',n)
	print('d 的值：',d)
	for key in d:
		total = total + d[key]
		print('*d:',key)

	return total

print('------第1次调用结果------')
result1=my_sum4(1,2)
print(result1)
print('------第2次调用结果------')
result2=my_sum4(1,2,3,4,5)
print(result2)
print('------第3次调用结果------')
result3=my_sum4(1,2,3,4,5,male = 6,femal = 7)
print(result3)


