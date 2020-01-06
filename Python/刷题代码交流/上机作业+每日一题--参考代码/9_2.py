#题目：输入某年某月某日，判断这一天是这一年的第几天？ 

#第一种方式：普通方式
# year = int(input('year:\n')) 
# month = int(input('month:\n')) 
# day = int(input('day:\n'))   
# months = (0,31,59,90,120,151,181,212,243,273,304,334) 
# if 0 <= month <= 12:      
# 	sum_day = months[month - 1] 
# else:      
# 	print('data error') 
# sum_day += day 
# leap = 0  
# if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):     
# 	leap = 1  
# 	if (leap == 1) and (month > 2):     
# 		sum_day += 1  
# 		print('it is the {0}th day.'.format(sum_day))

# 第二种方式：函数方式
# (1) judge leap year
def judge_leap_year(n):
     if (n%4 == 0 and n%100 != 0) or (n%100 == 0 and n%400 == 0):
         return True
     else:
         return False
# (2) computing the sum days of any day(**.**.**)
def compute_year_counts(datestr):
    # deal with these case:
    # 2012.12.2
    # 2012/12/2
    # 2012-12-2
    if datestr.find('.') > 0: date = datestr.split('.')
    if datestr.find('/') > 0: date = datestr.split('/')
    if datestr.find('-') > 0: date = datestr.split('-')
 
    year = int(date[0])
    month = int(date[1])
    day = int(date[2])
    if (month < 1 or month > 12):
        print("the error month!")
        return -1
    if (day > 31):
        print("the error day!")
        return -1
 
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
 
    nDays = sum(days[i] for i in range(0, month - 1))
    if (judge_leap_year(year)):
             nDays += 1
    return (nDays + day) 
 
datestring = input("input the datetime info:-->")
print(compute_year_counts(datestring))
