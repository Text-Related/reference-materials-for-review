#普通程序员的简单生活
#计算一个程序员的基本工资收入（纯整数运算）
salary = 25000
sa_total  = 0
sa_year   = 0

for i in range(40):
    sa_year  = salary * 12
    sa_total = sa_total + sa_year
    print(str.format('第 {0:2} 年，月工资 {1:6} ,年收入 {2:10} 元',i,salary,sa_year))
    
print('-------------------------------')
print(str.format('一生工资总收入 {0} 元',sa_total))
print('-------------------------------')
print('收入数据类型（sa_total）：',type(sa_total))

