#生成器实现
def fib():
    a,b=0,1
    while 1:
        a,b=b,a+b
        yield a  # 实现f(n)=f(n-1)+f(n-2)

#主程序
fibs=fib()
print('fibs类型：',type(fibs))
for f in fibs:
    if f<1000:
        print(f,end=',')
    else:
        break
