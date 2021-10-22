from urllib3 import *
disable_warnings()
http = PoolManager()
#url = 'https://www.baidu.com'
#url = 'http://httpbin.org/delay/3'
response = http.request('GET', url,timeout=Timeout(connect=2,read=4))
print(response.info())
print('------------')
print(response.info()['Content-Length'])
