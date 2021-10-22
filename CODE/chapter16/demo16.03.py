from urllib3 import *
import re
disable_warnings()
http = PoolManager()

url = 'https://list.tmall.com/search_product.htm?spm=a220m.1000858.1000724.4.53ec3e72bTyQhM&q=%D0%D8%D5%D6&sort=d&style=g&from=mallfp..pc_1_searchbutton#J_Filter'
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
data = response.data.decode('GB18030')
print(data)

