# -*- coding: utf-8 -*-
#输入出生日期（哪月哪日），输出属于哪个星座
#采用函数方式

def Zodiac(month, day):
	constellations = ('摩羯座','水瓶座','双鱼座','白羊座','金牛座','双子座','巨蟹座','狮子座','处女座','天秤座','天蝎座','射手座')
	date = ((1,20),(2,19),(3,21),(4,20),(5,21),(6,22),(7,23),(8,23),(9,23),(10,24),(11,23),(12,22))
	choice = date[month-1]  #python 下标从0开始，所以输入月份后，从date中取对应的元组数据（month,day)时，下标要减1（即month-1)
	if day < choice[1]:     #取出对应的元组（月，日）后，再取日期，从日期进行判断，
		return constellations[month -1]  #小于日期的，属于constellations对应位置的前一个星座
	else:
		return constellations[month]     #大于日期的，属于constellations对应位置的当前的星座

print("Enter your birthdate(month,day):")
month = int(input("Month:"))
day = int(input("Day:"))
constellation = Zodiac(month, day)
print("Your constellation is ：{0}".format(constellation))
