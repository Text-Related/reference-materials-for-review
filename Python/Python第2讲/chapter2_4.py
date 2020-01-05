# -*- coding: utf-8 -*-
#声明和调用函数方式
def computing_cost(money,year):
	return  money * year *12

Total_cost = 0

infant = float(input("婴儿期每月费用："))
baby = computing_cost(infant,3)

kinder = int(input("幼儿园每月费用："))
kindergarten = computing_cost(kinder,3)

primary = int(input("小学每月费用："))
primary_school = computing_cost(primary,6)

middle = int(input("初中每月费用："))
middle_school = computing_cost(middle,3)

high = int(input("高中每月费用："))
high_school = computing_cost(high,3)

college_fee = float(input("大学每月费用："))
colege = computing_cost(college_fee,4)

Total_cost = (baby + kindergarten + primary_school + middle_school 
            + high_school + college)

print(Total_cost)


