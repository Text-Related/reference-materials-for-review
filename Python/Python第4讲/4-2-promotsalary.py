salary=int(input("请输入有固定工资收入的党员的月工资:"))
⁭sa_tax=0
if(salary<=400):
    sa_tax=salary*0.005
else:
    if(salary>=401 and salary<=600):
        sa_tax=salary*0.01
    else:
        if(salary>=601 and salary<=800):
            sa_tax=salary*0.015
        else:
            if(salary>=801 and salary<=1500):
                sa_tax=salary*0.02
            else:
                sa_tax=salary*0.03
print("有固定工资收入的党员的月工资为：{0}".format(salary))
print("缴纳党费为:{0:.2f}".format(sa_tax))

