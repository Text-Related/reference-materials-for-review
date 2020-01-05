# -*- coding: utf-8 -*-
#计算某一年是否为闰年

try:  
  year = int(input("请输入年份(如2008): "))  
except:  
  print("请输入正确的年份")  
  exit() 

if (year%400 == 0):
	print("{0}是闰年".format(year))
elif(year%4 !=0):
	print("{0}不是闰年".format(year))
elif(year%100 == 0):
	print("{0}不是闰年".format(year))
else:
	print("{0}是闰年".format(year))

#使用一个逻辑表达式包含所有闰年条件
# if (year%4 ==0 and year%100 != 0) or (year%400 == 0):
# 	print("{0}是闰年".format(year))
# else:
# 	print("{0}不是闰年".format(year))

