n = int(input('please enter the num:'))
total = 1
for i in range(1,n+1):
	total = total * i
result = total
print('{0}! = {1}'.format(n,result))
