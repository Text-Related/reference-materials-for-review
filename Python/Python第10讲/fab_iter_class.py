class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a
    def __iter__(self):
        return self

#主程序
fibs = Fibs()
print('迭代器返回对象类型及对象地址：',type(fibs),fibs)
for i in fibs:
    if i <100:
        print(i)
    else:
        break

# #测试__next__和__iter__()方法
# print(fibs.__next__())
# print(fibs.__next__())
# print(fibs.__next__())

# for i in fibs.__iter__():
#     if i > 20:
#         break
#     else:
#         print(i, end = ' ')




