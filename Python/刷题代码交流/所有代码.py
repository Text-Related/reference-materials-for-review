##---------------------菲波那切数列
s=[]
a=1
b=1
c=0
s.append(a)
s.append(b)
for i in range(0,57):
    c=s[i]+s[i+1]
    s.append(c)
print(s[5])
##-------------------------------------------------------

import math
k=0
def sushu(n):
    k=int(math.sqrt(n))
    if n<=1: return False
    for i in range(2,k+2):
        if n%i==0:
           break
    if i==k+1:
      return True
   
for i in range(2,100):
   if  sushu(i):
       print(i)




##------------------------打印（1,100000）以内的素数
import math
k=0
def sushu(n):
    if n<=1:
        return False
    k=int(math.sqrt(n))
    for i in range(2,k+2):
        if n%i==0:
           break
    if i==k+1:
      return ("yes")
    else:
      return ("no")
    
for i in range(2,100000):
    if (len(sushu(i))==3):
        print(i)
##------------------------------------------- 
##--------------------------求1+2！+3！+4！+5！

a=1
sum=1
for i in range (2,4):
     for j in range(1,i+1):
         a*=j
     sum+=a
     a=1
print(sum)
##--------------------------------------------------
##---------------------------给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
a=int(input("输入一个不超过五位数的正整数:"))
c=0
c=a//10000
if (c!=0):
    print("万位上的数为：",c)
d=0
d=a//1000-c*10
if(d!=0):
    print("千位上的数为：",d)
e=0
e=a//100-c*100-d*10
if(e!=0):
    print("百位上的数为：",e)
f=0
f=a//10-c*1000-d*100-e*10
if(f!=0):
    print("十位上的数为：",f)
g=0
g=a-c*10000-d*1000-e*100-f*10
print("个位上的数为：",g)
a=str(a)
b=len(a)
print("这是一个{0}位数".format(b))
##----------------------------------------------------------
##---------输入n为偶数时，求1/2+1/4+...+1/n,当输入n为奇数时，求1/1+1/3+...+1/n，并打印结
s=0
m=0
n=int(input("请输入一个正整数："))
if(n%2==0):
    for i in range(2,n+2,2):
        s+=(1/i)
    print(s)
else:
    for j in range(1,n+1,2):
        m+=(1/j)
    print(m)
##------------------------------------------------------------------------------------

##---------------------------有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？请打印输出。 
##-----------------思路提示：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
s=[]
n=0
for i in range(1,5):
    for j in range(1,5):
        for k in range (1,5):
            n=i*100+j*10+k
            s.append(n)
m=[]
for i in range (1,5):
    for j in range(1,5):
        a=i*100+i*10+j
        b=i*100+j*10+i
        c=j*100+i*10+i
        m.append(a)
        m.append(b)
        m.append(c)
for i in range(1,65):
    if (s[i] not in m):
        print(s[i])
##---------------------------------------------------------------------------------------
##--------------------------输入两个正整数m和n，求其最大公约数和最小公倍数。        
s=[]
m=int(input("请输入一个正整数m:"))
n=int(input("请输入一个正整数n:"))
for i in range(1,m+1):
    if m%i==0:
        s.append(i)
a=len(s)
print(a)
for j in range (0,a):
    if n%s[j]==0 and s[j]<=n:
     k=s[j]
b=m*n/k
b=int(b)
print("最大公约数是：",k)
print("最小公倍数是: ",b)

##--------------------------------------------------------------------------------------------