from urllib3 import *
import re
import threading
disable_warnings()
http = PoolManager()

f = open('urls.txt','r')
urlList = []
while True:
    url = f.readline()
    if url == '':
        break;
    urlList.append(url.strip())
f.close()


class DownloadThread(threading.Thread):
    def __init__(self, func, args):
        super().__init__(target=func,args=args)

def download(filename,url):
    response = http.request('GET', url)
    f = open(filename,'wb')
    f.write(response.data)
    f.close()
    print('<',url,'>','下载完成')
for i in range(len(urlList)):
    thread = DownloadThread(download,(str(i) + '.jpg',urlList[i]))
    thread.start()