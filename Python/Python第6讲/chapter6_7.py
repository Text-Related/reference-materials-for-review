import pickle
try:
    f = open(r'd:\dataOjb1.dat','rb')
    o1 = pickle.load(f)
    o2 = pickle.load(f)
    o3 = pickle.load(f)
    o4 = pickle.load(f)
    print('类型：',type(o1),'内容：',str(o1))
    print('类型：',type(o2),'内容：',str(o2))
    print('类型：',type(o3),'内容：',str(o3))
    print('类型：',type(o4),'内容：',str(o4))
finally:
    f.close()
