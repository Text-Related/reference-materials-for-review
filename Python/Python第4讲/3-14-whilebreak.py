#计算while break 语句

print('----------------------')
print('1.while语句程序正常循环')
i = 0
while(i<10):
    print('当前执行：',i)
    i+=1

print('----------------------')
print('2.while语句程序break中断')
i = 0
while(i<10):
    print('当前执行：',i)
    i+=1
    if(i>=5): break


print('----------------------')
print('3.while语句程序continue跳过')
i = 0
while(i<10):
    i+=1
    if(i%2==0): continue
    print('当前执行：',i)

print('----------------------')
