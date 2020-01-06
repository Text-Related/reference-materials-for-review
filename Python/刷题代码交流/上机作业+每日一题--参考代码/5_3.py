#coding = utf-8
dic = dict()
dic['1001'] = '张三'
dic['1002'] = '李四'
dic['1003'] = '赵五'

stu_num = '1002'
print(dic.get(stu_num))

name = '赵五'

for item in dic.items():
	if item[1] == name:
		print('Yes')
		print(item[0])