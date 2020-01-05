#上三角
f = open('d:\\mult-9-9-up.txt','w')
for i in range(1,10):
	s = ' ' 
	for j in range(i,10):
		s += '{0}*{1}={2}'.format(i,j,i*j) + ' '
	s = s.rjust(60)
	f.write(s)
	f.write('\n')
	print(s)
f.close()
