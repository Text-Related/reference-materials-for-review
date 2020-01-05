# -*- coding: utf-8 -*-
#import numpy as np
dis = [[0, 41.99, 46.03, -1],
 [41.99, 0, 24.85, 24.3],
 [46.03, 24.85, 0, 10.5],
 [-1, 24.3, 10.5, 0]]

m = [2,2,3]

def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step

def cost(x1, y1, z1, x2, y2, z2, m1, n1, p1, m2, n2, p2):
    cost = 0
    cost += dis[2][3]*(m[0]*x1+m[1]*y1+m[2]*z1)
    cost += dis[1][3]*(m[0]*x2+m[1]*y2+m[2]*z2)
    cost += dis[0][2]*(m[0]*m1+m[1]*n1+m[2]*p1)
    cost += dis[0][1]*(m[0]*m2+m[1]*n2+m[2]*p2)
    return cost

#count = 0
#costList = []
#arrange = []
#
#for a in frange(1, 7, 0.1):
#    for b in frange(1, 3, 0.1):
#        for c in frange(1, 5, 0.1):
#            p4 = [a, b, c]
#            p1 = [6-a, 2-b, 4-c]
#            for x1 in frange(0, a + 1, 0.1):
#                y1 = b - 1
#                z1 = 0
#                x2 = a - 2 - x1
#                y2 = 0
#                z2 = c - 2
#                m1 = 1 - x1
#                n1 = 1 - y1
#                p1 = 0
#                m2 = 2 - x2
#                n2 = 0
#                p2 = 1 - z2
#                if y1 >= 0 and x2 >= 0 and z2 >= 0 and m1 >= 0 and n1 >= 0 and m2 >= 0 and p2 >= 0:
#                    arr = [a,b,c]
#                    arrange.append(arr)
#                    t = cost(x1, y1, z1, x2, y2, z2, m1, n1, p1, m2, n2, p2)
#                    costList.append(t)
##                    print("a, b, c:", a, b, c)
##                    print("x1, y1, z1:", x1, y1, z1)
##                    print("x2, y2, z2:", x2, y2, z2)
##                    print("m1, n1, p1:", m1, n1, p1)
##                    print("m2, n2, p2:", m2, n2, p2)
#                    count = count + 1
#print("count:",count)
#print("min cost:",min(costList))
#min_index = costList.index(min(costList))
#print("min arrange:",arrange[min_index])
                
a=5
b=2
c=3
p4 = [a, b, c]
p1 = [6-a, 2-b, 4-c]
for x1 in frange(0, a + 1, 0.1):
    y1 = b - 1
    z1 = 0
    x2 = a - 2 - x1
    y2 = 0
    z2 = c - 2
    m1 = 1 - x1
    n1 = 1 - y1
    p1 = 0
    m2 = 2 - x2
    n2 = 0
    p2 = 1 - z2
    if y1 >= 0 and x2 >= 0 and z2 >= 0 and m1 >= 0 and n1 >= 0 and m2 >= 0 and p2 >= 0:
        t = cost(x1, y1, z1, x2, y2, z2, m1, n1, p1, m2, n2, p2)
        print(t)