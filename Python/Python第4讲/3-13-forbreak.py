#计算for break 语句

print('----------------------')
print('1.for语句程序正常循环')
for i in range(10):
    print('当前执行：',i)

print('----------------------')
print('2.for语句程序break中断')
for i in range(10):
    if(i>=5): break
    print('当前执行：',i)


print('----------------------')
print('3.for语句程序continue跳过')
for i in range(10):
    if( i%2 == 0 ): continue
    print('当前执行：',i)
