n=int(input('请输入整数1='))
m=int(input('请输入整数2='))
s=m*n
while m!=n:
    if m>n:
        m=m-n
    else:
        n=n-m
print(m)
i=s//m
print(i)
