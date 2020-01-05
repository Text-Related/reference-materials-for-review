#下三角
f = open('d:\\mul9-9-down.txt','w')
for i in range(1,10):
	s = ''
	for j in range(1,i+1):
		s += '{0}*{1}={2}'.format(i,j,i*j) + ' '
	print(s)
	f.write(s)
	f.write('\n')
f.close()
