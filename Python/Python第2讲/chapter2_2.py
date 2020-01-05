# -*- coding: utf-8 -*-
#带输入输出的数学计算

Total_cost = 0

infant = int(input("婴儿期每月费用："))
baby = infant * 12 * 3 

kinder = int(input("幼儿园每月费用："))
kindergarten = kinder * 12 * 3

primary = int(input("小学每月费用："))
primary_school = primary * 12 * 6

middle = int(input("初中学每月费用："))
middle_school = middle * 12 * 3

high = int(input("高中每月费用："))
high_school = high * 12 * 3

college_fee = int(input("大学每月费用："))
college = college_fee * 12 * 3

Total_cost = (baby + kindergarten + primary_school + middle_school 
            + high_school + college)

print(Total_cost)



