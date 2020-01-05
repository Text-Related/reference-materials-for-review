#计算三角形面积代码： (带三边规则的逻辑判断)
import math

a=20  ;#a=float(input("请输入三角形的边长a:"))
b=30  ;#b=float(input("请输入三角形的边长b:"))
c=40  ;#c=float(input("请输入三角形的边长c:"))
print("第三讲：代码实例3，分支结构-三角形面积")
p=(a+b+c)/2

if( a>0 and b>0 and c>0 and p>a and p>b and p>c):
      print("恭喜：符合三角形三边规则！")
      area=math.sqrt(p*(p-a)*(p-b)*(p-c))
      print(str.format("  三角形三边分别为：a={0},b={1},c={2}",a,b,c))
      print(str.format("  三角形面积={0}",area))
      
print("第三讲：代码实例3，分支结构-执行完毕")
