#输入杨辉三角的层数（深度）
n = int(input('Please enter the depth of the triangle: '))

for i in range(n):
        if i == 0:
                ls = [[1]]
        elif i == 1:
                ls = [[1],[1,1]]
        else:
                t_ls = []       #每次要计算一个List，先置空
                t_ls.append(1)  #第一个值为1
                tem = ls[i-1]   #获取上一行的值，用于下一行计算
                for j in range(1,i):   #从第二个值开始计算，至倒数第二个值停止
                        t_ls.append(tem[j-1] + tem[j])  #当前值等于上一行同列的值与前一列的值之和
                t_ls.append(1)  #最后一个值为1
                ls.append(t_ls) #将

#输出，类似九九表
for i in range(len(ls)):
	s = ''
	a = ls[i] #先取一行，每一行就是一个list
	for j in range(len(ls[i])):
		s += str.format('{0:4}',a[j])   #再将这个list中的每个值输出，并转成字符串格式
	print(s.center(40))  #字符串居中
