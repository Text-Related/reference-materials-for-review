m=int(input('请输入一个正整数：'))
n=int(input('请再输入一个正整数：'))
a=max(m,n)
b=min(m,n)
c=a%b
if c==0:
    print('它们的最大公约数为：',b)
    print('它们的最小公倍数为：',a)
else:
    while c>0:
        a=b
        b=c
        c=a%b
    print('它们的最小公约数为：',b)
    print('他们的最小公倍数为',int((m/b)*(n/b)*b))
