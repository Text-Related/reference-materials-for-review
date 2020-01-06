#s=a+aa+aaa+aa….a
n = 5;a = 2
s = 0;t = a
for i in range(5):
	s += t
	print('t = {0}, sum = {1}'.format(t,s))
	t = t*10 + a
	

