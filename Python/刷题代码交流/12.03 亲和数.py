list = []
for i in range(1000,9999):
    m=0
    for j in range(2,i):
        if i%j == 0:
            m = m+j
    list.append(m)
#print(list)

for n in range(len(list)):
    for w in range(len(list)):
        if (n > w and list[n]== w+1000 and list[w]==n+1000 and list[n]!=0):
            print(str.format('{0:4}和{1:4}互为一对亲和数',n+1000,w+1000))
