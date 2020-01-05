# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 17:28:04 2019

@author: sqsje
"""

dis = [[0, 41.99, 46.03, -1],
 [41.99, 0, 24.85, 24.3],
 [46.03, 24.85, 0, 10.5],
 [-1, 24.3, 10.5, 0]]

m = [2,2,3]

def lineCost(dis, n1, n2, n3):
    return dis * (m[0]*n1+m[1]*n2+m[2]*n3)

def totalCost(a, b, c):
    totalcost = 0
    totalcost = totalcost+dis[0][2]*(m[0]*1+m[1]*0+m[2]*1)
    totalcost = totalcost+dis[1][2]*(m[0]*2+m[1]*0+m[2]*1)
    totalcost = totalcost+dis[3][2]*(m[0]*2+m[1]*1+m[2]*2)
    return totalcost

a = 6
b = 2
c = 4
#for a in range(2,5):
#    for c in range(1,3):
print("a,b,c:",a,b,c)
print("~a,~b,~c:",6-a,2-b,4-c)
print(totalCost(a,b,c))