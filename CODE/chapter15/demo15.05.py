from socket import *
import os
def responseHeaders(file,length):
    f = open(file,'r')
    
    headersText = f.read()
    headersText = headersText % length
    return headersText

def filePath(get):
    if get == '/':
        return 'static' + os.sep + 'index.html'
    else:
        paths = get.split('/')
        s = 'static'
        for path in paths:
            if path.strip() != '':
                s = s + os.sep + path 
        return s
host = ''
bufferSize = 1024
port = 9876
addr = (host,port)
tcpServerSocket = socket(AF_INET, SOCK_STREAM)
tcpServerSocket.bind(addr)
tcpServerSocket.listen(5)
while True:
    print('正在等待客户端连接')
    tcpClientSocket,addr = tcpServerSocket.accept()
    print('客户端已经连接','addr','=','addr')
    data = tcpClientSocket.recv(bufferSize)
    data = data.decode('utf-8')
    try:
        firstLine = data.split('\n')[0]
        path = firstLine.split(' ')[1]
        print(path)
        path = filePath(path)
        if os.path.exists(path):
            file = open(path,'rb')
            content = file.read()
            file.close()        
        else:
            content = '<h1>File Not Found</h1>'.encode(encoding='utf-8')
        rh = responseHeaders('response_headers.txt',len(content)) + '\r\n'        
        tcpClientSocket.send(rh.encode(encoding='utf-8') + content)
            
    except Exception as e:
        print(e)
    tcpClientSocket.close()
tcpServerSocket.close();
        