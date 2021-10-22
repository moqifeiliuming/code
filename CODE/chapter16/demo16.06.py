from urllib3 import *
disable_warnings()
http = PoolManager(timeout=Timeout(connect=2,read=2))
url1 = 'https://www.baidu1122.com'
url2 = 'http://httpbin.org/delay/3'
try:
    http.request('GET', url1,timeout=Timeout(connect=2.0,read=4))
except Exception as e:
    print(e)
print('------------')
response = http.request('GET', url2,timeout=Timeout(connect=2,read=4))
print(response.info())
print('------------')
print(response.info()['Content-Length'])
http.request('GET', url2,timeout=Timeout(connect=2,read=2))