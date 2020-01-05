import math
k=0
def sushu(n):
    if n<=1:
        return False
    k=int(math.sqrt(n))
    for i in range(2,k+1):
        if n%i==0:
            return False
    return True
    
for i in range(2,1000000):
    if sushu(i):
        print(i)
    
