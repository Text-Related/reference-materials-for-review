class Person:                     # 基类
	def __init__(self,name,age):  # 构造函数
		self.name = name
		self.age = age
	def say_hi(self):
		print("Hello, My name is {0}, I'm {1}".format(self.name,self.age))

class Student(Person):            # 派生类
	def __init__(self,name,age,stu_id):
		Person.__init__(self,name,age)
		self.stu_id = stu_id
	def say_hi(self):
		Person.say_hi(self)
		print("I'm a student, My student ID is ",self.stu_id)

p1 = Person('Jack',30)
p1.say_hi()

p2 = Student('John',20,'201611210001')
p2.say_hi()



		
