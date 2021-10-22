from urllib3 import *
import re
disable_warnings()
http = PoolManager()

url = 'https://www.taobao.com/'
def str2Headers(file):
    headerDict = {}
    f = open(file,'r')
    headersText = f.read()
    headers = re.split('\n',headersText)
    for header in headers:
        result = re.split(':',header,maxsplit = 1)
        headerDict[result[0]] = result[1]
    f.close()
    return headerDict
headers = str2Headers('headers.txt')
response = http.request('GET', url,headers=headers)
result = re.search('charset=([^\)\']*)',response.info()['Content-Type'])
charset = result.group(1)

data = response.data.decode(charset)
print(data)

