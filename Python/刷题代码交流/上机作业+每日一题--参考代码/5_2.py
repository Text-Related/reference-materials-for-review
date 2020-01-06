str1 = 'this is  a test. 123  45678~ end!'

cout_alf,cout_dig,cout_space, cout_other = 0,0,0,0

for i in range(len(str1)):
	if str1[i].isalpha():
		cout_alf += 1
	elif str1[i].isdigit():
		cout_dig += 1
	elif str1[i].isspace():
		cout_space += 1
	else:
		cout_other += 1
print('total num:{0} \nletters:{1} \ndigitals:{2}'.format(len(str1),cout_alf,cout_dig))
print('space:{0} \nothers:{1}'.format(cout_space,cout_other))



