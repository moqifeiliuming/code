from urllib3 import *
disable_warnings()
http = PoolManager()
url = 'http://localhost:5000'
while True:
    filename = input('请输入要上传的文件名字（必须在当前目录下）：')
    if not filename:
        break
    with open(filename,'rb') as fp:
        fileData = fp.read()
    response = http.request('POST',url,fields={'file':(filename,fileData)})
    print(response.data.decode('utf-8'))
