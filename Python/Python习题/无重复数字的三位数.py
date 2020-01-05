a=int(input('请输入数a:'))
b=int(input('请输入数b:'))
c=int(input('请输入数c:'))
d=int(input('请输入数d:'))
s=[a,b,c,d]
l=[]
for i in s:
    for j in s:
        for k in s:
            if i!=j and i!=k and j!=k:
                m=i*10**2+j*10+k
                l.append(m)
                
print('可组成无重复数字的三位数：',l)
