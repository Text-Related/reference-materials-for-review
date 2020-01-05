# -*- coding: utf-8 -*-
#计算闰年
import math

year=2016

if(year%400==0):
        print("{0}是闰年".format(year))
elif(year%4 !=0):
        print("{0}不是闰年".format(year))
elif(year%100==0):
        print("{0}不是闰年".format(year))
else:
        print("{0}是闰年".format(year))
        

if((year%4==0 and year%100 !=0 ) or (year%400==0)):
        print("{0}是闰年".format(year))
else:
        print("{0}不是闰年".format(year))   
