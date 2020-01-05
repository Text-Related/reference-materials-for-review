a=input('请输入字符串A：')
b=input('请输入字符串B：')
if len(a)>=len(b):
    a,b=b,a
c=0
for j in range(len(a),-1,-1):
    for i in range(len(a)-j+1):
        s=a[i:i+j]
        if b.find(s)!=-1:
            c=c+1
            if c==1:
                print(s)
            else:
                break
