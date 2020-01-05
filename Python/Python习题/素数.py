m=int(input('请输入范围：'))

s=[]
l=[]

for i in range(2,m+1):
    s.append(i)
    for j in range(2,i):
        if i%j==0:
            l.append(i)
            break
        else:
            continue

n=[i for i in s if i not in l]

for i in range(len(n)):
    print(n[i])


        
    
       

