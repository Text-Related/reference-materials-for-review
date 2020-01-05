import requests
url="http://m.kdnet.net/cluster/list?clusterid=1"
try:
    r=requests.get(url,timeout=30)
    r.raise_for_status()
    r.encoding='utf-8'
    ptint(r.text)
except:
    print("")
