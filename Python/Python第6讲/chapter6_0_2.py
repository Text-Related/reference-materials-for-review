f1 = open(r'd:\myfile.txt','r')
s1 = f1.readline()       #读入1行内容
print(s1)
s2 = f1.readlines()      #读入剩余多行内容：
print(s2)
