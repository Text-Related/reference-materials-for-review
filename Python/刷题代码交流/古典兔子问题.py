n=int(input('输入月数：'))


def f(n):
    if n<=2:
        return(1)
    else:
        return(f(n-1)+f(n-2))
        

print('{0}个月后的兔子数为：{1}'.format(n,f(n)))