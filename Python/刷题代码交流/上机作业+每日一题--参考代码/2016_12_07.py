#题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月
#后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？ 
#程序分析： 兔子的规律为数列1,1,2,3,5,8,13,21.... ，这就是斐波那契数列

# 普通方式：
n = 10
f1 = 1; f2 = 1
for i in range(1,n+1):
	print(str.format('{0:20}{1:20}',f1,f2),end  = ' ')
	if i%2 ==0:
		print()
	f1 += f2
	f2 += f1

# #递归函数方式：
# def fab(num):
# 	if num == 0:
# 		return 1
# 	else:
# 		return num* fab(num-1)

# n = 10
# for i in range(n):
# 	print(fab(i), end = ' ')


 