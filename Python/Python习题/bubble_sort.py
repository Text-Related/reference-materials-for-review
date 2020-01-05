import random

s=[]
for r in range(10):
    s.append(random.randint(1,100))
print(s)

for i in range(len(s)):
    for j in range(i):
        while s[i]>s[j]:
            s[i],s[j]=s[j],s[i]
print(s)

#------------------------------------


for i in range(len(s)):
    for j in range(i):
        while s[i]<s[j]:
            s[i],s[j]=s[j],s[i]
print(s)
