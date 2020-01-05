# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 15:53:01 2016

@author: Administrator
"""


n=int(input('层数：'))
a=[[0]*(n+1)]*(n+1)
for i in range(n+1):
    for j in range(n+1):
        print(a[i][j],end="\t")
    print()
for i in range(0,n):
    for j in range(0,i+1):
        if i==0 or j==0:
            a[i][j]=1
            print(str(i)+"\t"+str(j)+"\t"+str(a[i][j]))
            #print(a[i][j],end='\t'
        elif i==j:
            a[i][j]=1
            print(str(i)+"\t"+str(j)+"\t"+str(a[i][j]))
        else:
            a[i][j]=(a[i-1][j-1]+a[i-1][j])
            print(str(i)+"\t"+str(j)+"\t"+str(a[i][j]))
            #print(a[i][j],end='\t')
    print()
print()