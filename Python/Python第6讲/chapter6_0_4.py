try:
    f=open(r'd:\myfile02.txt','r')
    s=f.readline()
    print(s)
    print('First line result Type is :',type(s))
    print('------------------------------------')

    lst=f.readlines()
    print(lst)
    print('Lines result Type is :',type(s))
    print('------------------------------------')

    for w in lst:
        print(w)
    
finally:
    f.close()
