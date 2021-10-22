from socket import *
from time import ctime
# 时间戳服务器
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
    print('客户端已经连接','addr','=',addr)
    while True:
        data = tcpClientSocket.recv(bufferSize)
        if not data:
            break;
        tcpClientSocket.send(ctime().encode(encoding='utf-8') + b' ' + data)
    tcpClientSocket.close()
tcpServerSocket.close();
        