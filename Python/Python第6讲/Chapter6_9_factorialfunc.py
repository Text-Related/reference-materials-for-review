#计算阶乘Chapter6_9.py
def factorial(n):
    if n == 0 or n == 1:
        return 1

    total = 1
    for i in range(2,n+1):
        total = total * i
    return total

n = int(input('please enter the num:'))
result = factorial(n)
print('{0}! = {1}'.format(n,result))
