# 12.06 每日一题，求亲和数
# 如果两个正整数a和b满足：a的所有除本身以外的因数之和等于b，b的所有除本身以外的因数之和等于a，则称a，b是一对亲和数。
# 现请你编一个程序找出所有由两个四位数组成的亲和数对。
# 实验指导：用穷举法解决该问题
# （1）确定变量穷举的范围[1000,9999]
# （2）计算因数和
# （3）判断因数和是否等于另一个数
# （4）如果两个数因数和分别等于另一个数，则输出这两个数，否则继续穷举
import time

def d(n):  #计算数字n所有真因数之和
    res = 0
    for i in range(1, n//2+1):
        if n/i == float(n//i):
            res += i
    return(res)

start = time.clock()

dic = dict()
for i in range(1000,10000):
    a = d(i)
    b = d(a)
    if b == i and b != a:
        dic[i] = a   

end = time.clock()

print(dic)
print('the processing time is:',end-start)


# #其他方式
# def  cal_factor(n):
# 	sum_n = 0
# 	for i in range(1,n):
# 		if (n%i == 0):
# 			sum_n += i
# 	return sum_n

# for i in range(1000,10000):
# 	a = cal_factor(i)  # i的因子和, 赋值给a
# 	b = cal_factor(a)  # i因子和这个数(a)的因子和,赋值给b
# 	if b == i and b != a:
# 		print('{0},{1}'.format(i,a))
