import os  #导入os模块
print('--------获取当前路径-----')
print(os.getcwd())  #获得当前路径
print()

print('------列出目录下所有文件和文件夹------')
print(os.listdir('d:\code'))
print()

print('----切换当前目录-----')
print(os.chdir(r'd:\code'))
print()

print('----创建一个名为hahaha的目录-----')
print(os.mkdir('justtest'))
print()

print('删除一个名为TEST的目录')
print(os.rmdir('TEST'))
print()

print('重命名一个文件')
print(os.rename('abc.txt','readme.txt'))
