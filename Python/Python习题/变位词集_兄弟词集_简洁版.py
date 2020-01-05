d=["abide","spot","abound","abreast","abstain","absurs","adore","adorn","advent","advers",
"at","baby","back","bacon","bad","badge","badly","ball","ban","bank","bar","cab","cabin",
"cable","cafe","cage","cake","call","calm","came","camp","dais","damn","damp","dance","danger",
"dark","dash","data","date","dawn","day","dead","deaf","deal","dean","dear","death","debt",
"deck","deer","each","eager","eagle","ear","early","earn","earth","ease",
"east","easy","eat","edge","edit","effect","effort","egg","ego","elder","elect",
"else","face","fact","factor","fade","fail","faint","fair","fake","fall","false","gain",
"game","gap","gate","gay","gaze","gear","gene","germ","get","hail","hair","half","hall",
"halt","ham","hand","hang","hard","said","tea","eat","nic","cin","ddc",
"dcd","abc","bac","pots","stop"]
keys=dict()
print('字典单词表:',d)

for i in d: # 字典内每个单词遍历
        arr2 =[]
        s1=''       
        for m in i:
            arr2.append(m)
            arr2.sort() # 将单词字母排序，构造字典关键字key
        for k in arr2:
            s1 +=k
        print(s1)
        

        oldarr = keys.get(s1) # 取关键字看是否已经有值
        if oldarr :            # 保留已有列表并追加当前单词
            oldarr.append(i)
            keys.setdefault(s1,oldarr) # 创建key并存入value
        else:
            valarr = []        # 新建列表存放关键字对应兄弟单词组
            valarr.append(i)
            keys.setdefault(s1,valarr)

def find(dictsim,searchword):
    s0=''
    arr1=[]
    for j in searchword:
        arr1.append(j)
        arr1.sort()
    for ch in arr1:
        s0 +=ch

    print('检索单词',searchword,'按字母排序key值：',s0)

    return dictsim.get(s0)


a=input('请输入单词:')
items=find(keys,a)
print(items)

        

