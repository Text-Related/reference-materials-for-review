# coding:utf-8
hobbies = "" 
for i in range(1, 4):
    s=input("请输入爱好之一（最多三个，按Q或q结束）:")
    if s.upper()=='Q':
        break
    hobbies += s + ','
else:
    print("你输入了三个爱好。")
print("你的爱好是：", hobbies)

