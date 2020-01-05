#计算出错情况的try...except处理
#i=100*200
#j=i/0
try:
    i=100*200
    #j=i/0
except:
    print('注意：出现执行错误，请检查输入和数据')
else:
    print('祝贺：程序正常结束，无任何致命错误')
finally:
    print('Try 代码执行完毕，执行finally语句')


