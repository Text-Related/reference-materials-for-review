#**********求亲和数**********
#**********12-03*************
#*****感谢张逸涵同学代码******
#

for i in range(1000,10000): # 循环测试所有4位数是否符合
    s=[]
    for j in range(2,i):    # 计算当前i值的所有因子之和
        if i%j == 0:
            s.append(j)
        b=sum(s)
        
    if b >= 10000 or b<1000: #判断是否满足4位数条件
        continue

    d=[]    
    for m in range(2,b):    # 计算i的所有因子之和b值的所有因子和    
        if b%m == 0:
            d.append(m)
        c=sum(d)
        
    if c==i :               # 判断两个数因子和是否互为对方
        print('亲和数是{0},{1}'.format(i,b))
