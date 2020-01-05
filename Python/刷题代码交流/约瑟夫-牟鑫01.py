n=int(input())
a=int(input())
m=int(input())
name=[]
for i in range(n+1):
    name.append(i)

def f(name,a,m,n): 
    if n==1:
        print(name[1])
    else:
        if (a+m-1)%n==0:
            print(name[n])
            del name[n]
            n-=1
            f(name,n,m,n)
        else:
            print(name[(a+m-1)%n]) 
            del name[(a+m-1)%n]
            n-=1
            f(name,(a+m-1)%n,m,n)
            
        
                 
f(name,a,m,n)
        
    


    