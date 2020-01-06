ls = [1,1]
def fact(n):
	for j in range(2,n):
		tem1 = ls[j-1]
		tem2 = ls[j-2]
		ls.append(tem1+ tem2)
	return ls

lst = fact(20)
s = ''
for i in range(20):
	s += '{0:5}'.format(lst[i])
	if (i+1)%10 == 0:
		print(s)
		s = ''

