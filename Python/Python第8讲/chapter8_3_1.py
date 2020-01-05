class Person2:                     # 定义类Person          
	def __init__(self,name,age):   # __int__方法
		self.name = name           # 初始化属性name
		self.age = age             # 初始化属性age

	def say_hi(self):
		print('Hello, my name is:',self.name)  #通过self.name访问

p1 = Person2('Jack',25)    # 创建对象
p1.say_hi()      # 调用对象的方法
print(p1.age)    # 通过p1.age(obj.变量名)读取成员变量