h=int(input('请输入高度:'))
t=int(input('请输入反弹次数:'))
s=0
for i in range(1,t+1):
    s=s+h*(1/2)**i
    print(h*(1/2)**i)
print(s)
l=h*(1/2)**t
print(l)
