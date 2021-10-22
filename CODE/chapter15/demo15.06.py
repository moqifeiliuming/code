from socket import *
# 客户端Socket
host = 'localhost'
port = 9876
bufferSize = 1024
addr = (host,port)
tcpClientSocket = socket(AF_INET, SOCK_STREAM)
tcpClientSocket.connect(addr)
while True:
    data = input('>')
    if not data:
        break
    data = data.encode('utf-8')
    tcpClientSocket.send(data)
    data = tcpClientSocket.recv(bufferSize)
    print(data.decode('utf-8'))
tcpClientSocket.close()