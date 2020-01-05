try:
    f1 = open(r'd:\databin2.dat','wb')
    f1.write(b'123')
    f1.write(b'abc')
    #f1.write(b'你好')
finally:
    f1.close()
