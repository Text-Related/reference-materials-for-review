b=input('请输入一个表示整数的字符串：') 
a=int(b)

print(a)

#-----------------------------

print(b[::-1]) 


#------------------------------
s=[]
a_=0
for i in range(1,len(b)+1):
    c=a%10**i
    d=c//10**(i-1)
    s.append(d)
for j in range(len(s)):
    a_+=s[len(s)-j-1]*10**j
print(a_)
