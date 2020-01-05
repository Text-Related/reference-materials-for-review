#求因数和
def y(n):
    l=[]
    for m in range (2,n):
        if n%m==0:
            l.append(m)
    return sum(l)


#确定范围
for i in range(1000,10000):
    if y(i)>=10000 or y(i)<1000:
        continue
#判断、输出亲和数
    if y(y(i))==i and i<y(i):
        print('{0}和{1}是一对亲和数'.format(i,y(i)))
            
        
