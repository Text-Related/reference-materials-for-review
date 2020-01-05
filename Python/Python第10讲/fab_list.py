def fab(max):
    n, a, b = 0, 0, 1
    L = []
    while n < max:
        L.append(b)
        a,b = b,a + b
        n = n + 1
    return L

Lst = fab(5)
print('type result:',type(Lst))
print(Lst)
