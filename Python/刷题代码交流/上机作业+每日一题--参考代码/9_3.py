#coding=utf8
'''
题目：0，1，...，n-1这n个数字排成一个圆圈，从数字a开始每次从这个圆圈里删除第m个数字。求出这个圆圈里删除数字的顺序。
按照顺时针和逆时针交替进行的方式
'''
import time

def solve(n,a,m):  
    lst = [x for x in range(n)]  
    k=(m-1+a)%n; 
    count = 0
    while(len(lst) >1):
    	print(lst[k]+1, end = ' ')
    	count += 1
    	del lst[k]
    	if count%2 == 0:
    		k= (k+m-1) % len(lst) 
    	else:
    		k= (k-m) % len(lst)  
    print(lst[0]+1)

start = time.clock()
solve(10,3,2)
end = time.clock()
print('the processing time is:',end-start)
