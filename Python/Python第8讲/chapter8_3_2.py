class Person3:
	count = 0  #类变量
	def __init__(self,name,age):
		self.name = name
		self.age = age
		Person3.count += 1   # 创建一个实例时，计数加1
	def __del__(self):
		Person3.count -= 1   # 销毁一个实例时，计算减1

	def  say_hi(self):
		print('Hello, my name is :',self.name)

	def get_count():    #创建类方法
		print('The total count is :',Person3.count)
		
	def get_count1(self):    #创建类方法
		print('The self count is :',self.count)

print('Total count is :',Person3.count)  #类名访问

p31 = Person3('Jack',25)     # 创建对象
p31.say_hi()                 # 调用对象的方法
Person3.get_count()          # 通过类名访问
p31.get_count1()

P32 = Person3('John',28)    
P32.say_hi()
Person3.get_count()
P32.get_count1()

del p31                      # 删除对象
Person3.get_count()
del P32
Person3.get_count()
