#---- 12.02每日一刷1000000以内的素数----
import math

n=3
s='     2 ,     3 ,     5 ,'
for i in range(3,1000000,2): # 2-1000000内所有数字判断素数，跳过偶数
    if(i%5000 == 1 ):        # 每5000个数，打印一次结果
        print('----------------',i,'-------------')
        print(s)
        s=''                 # 打印完清空
    elif i % 5 == 0:         # 跳过5的倍数
        continue;   
    
    rt=int(math.sqrt(i))

    for j in range(2,rt+1):  # 2-当前i的平方根，判断是否为因子
        if( i%j == 0):       # 找到因子终止当前i素数测试
            break;
        elif j == rt :       # 到平方根，仍未找到因子为素数
            s +=str.format('{0:6} ,',i)
            n+=1
print(s) #打印最后一组素数
print('end-素数个数：',n)
    
        
        
       
