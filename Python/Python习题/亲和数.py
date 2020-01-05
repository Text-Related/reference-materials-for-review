for i in range(1000,10000):
    s=[]
    for j in range(2,i):   
        if i%j == 0:
            s.append(j)
        b=sum(s)
        
    if b >= 10000 or b<1000: 
        continue

    d=[]    
    for m in range(2,b):        
        if b%m == 0:
            d.append(m)
        c=sum(d)
        
    if c==i :               
        print('亲和数是{0},{1}'.format(i,b))
