from urllib3 import *
from urllib.parse import urlencode

disable_warnings()
http = PoolManager()
url = 'http://www.baidu.com/s?' + urlencode({'wd':'极客起源'})
print(url)
#response = http.request('GET', url)
url = 'http://www.baidu.com/s'
response = http.request('GET', url,fields={'wd':'极客起源'})
data = response.data.decode('UTF-8')
print(data)

