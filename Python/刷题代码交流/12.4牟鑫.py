s=0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i!=j and i!=k and j!=k:
                s+=1
                print('{0}{1}{2}'.format(i,j,k))
print(s)