for i in range (1000,10000):
    s=[]
    d=[]
    for j in range (2,i):
        if i%j==0:
            s.append(j)
        b=sum(s)
    if b>=10000 or b<1000:
        continue
    for m in range(2,b):
        if b%m==0:
            d.append(m)
        c=sum(d)
    if c==i and i<b:
        print('{0}和{1}是一对亲和数'.format(i,b))
        
        
        
