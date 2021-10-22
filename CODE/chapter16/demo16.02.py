from urllib3 import *


disable_warnings()
http = PoolManager()

url = 'http://localhost:5000/register'
response = http.request('POST', url,fields={'name':'李宁','age':18})
data = response.data.decode('UTF-8')
print(data)

