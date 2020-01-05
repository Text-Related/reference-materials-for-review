n=int(input("几个人玩："))
a=int(input("从谁开始报："))
m=int(input("报到几的人出局："))
s=[]
for i in range(1,n+1):
    s.append(i)
print(s)
count=0
while(len(s)>0):
    count+=1
    if(count%2!=0):
        boom=(a-1+m-1)%len(s)
        print(s[boom])
        s.pop(boom)
        a=boom
        print(s)
        
    if(count%2==0):
        boom=(a-m)%len(s)
        print(s[boom])
        s.pop(boom)
        a=boom+1
        print(s)
