# 每日刷题 12-07
# 构造兄弟单词字典，以相同单词的字母顺序排序字串为关键字
# 例如：{'opst':['stop','spot']}
def builddicts(pathname):
    dict1=dict()
    with open(pathname,'r') as f:
        srcarr=f.read()
    srcarr = srcarr.replace('\n','')
    srcarr = srcarr.replace('"','')
#    print(srcarr)   # 打印原始字典文件内容    

    wdsarr = srcarr.split(',')
    print('字典单词表:',wdsarr)   # 打印拆分后的字典单词表

    for d in wdsarr: # 字典内每个单词遍历
        arr2 =[]
        s1=''        # 将单词字母排序，构造字典关键字key
        for m in d:
            arr2.append(m)
            arr2.sort()
        for k in arr2:
            s1 +=k

        oldarr = dict1.get(s1) # 取关键字看是否已经有值
        if oldarr :            # 保留已有列表并追加当前单词
            oldarr.append(d)
            dict1.setdefault(s1,oldarr)
        else:
            valarr = []        # 新建列表存放关键字对应兄弟单词组
            valarr.append(d)
            dict1.setdefault(s1,valarr)
        
    return dict1

# 根据给定检索单词，输出相似的兄弟单词组
def findwd(dictsim,searchword):

    s0=''
    arr1=[]
    for i in searchword:
        arr1.append(i)
        arr1.sort()
    for ch in arr1:
        s0 +=ch

    print('检索单词',searchword,'按字母排序key值：',s0)

    return dictsim.get(s0)


#主程序部分
#构造兄弟词字典
dict_a = builddicts(r'd:/code/dictwords.txt')
wdusr=input('请输入单词：')
wdrst = findwd(dict_a,wdusr)
print(wdrst)

            

    
        
        
