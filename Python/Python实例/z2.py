import requests
r = requests.get(url='http//m.kdnet.net/cluster/list?clusterid=1', params={'wd':'python'})   #带参数的GET请求
print(r.url)
print(r.text)   #打印解码后的返回数据