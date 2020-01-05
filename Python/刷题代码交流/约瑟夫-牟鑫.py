n=int(input())
a=int(input())
m=int(input())
name=[]
for i in range(n+1):
    name.append(i)
k=1
def f(name,a,m,n,k):
    if n==1:
        print('survivor:',name[1])
    else:
        if k>0:
            d=(a+m-1)%n
            if d==0:
                d=n
            print('kill:',name[d])
            del name[d]
            n-=1
            k*=-1
            f(name,d,m,n,k)
        
        else:
            d=(a-m)%n
            if d==0:
                d=n
            print('kill:',name[d])
            del name[d]
            n-=1
            k*=-1
            f(name,d,m,n,k)
    
    
f(name,a,m,n,k)
    
          

        
    


    