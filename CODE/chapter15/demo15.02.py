from socket import *

host = ''
bufferSize = 2
port = 9876
addr = (host,port)
tcpServerSocket = socket(AF_INET, SOCK_STREAM)
tcpServerSocket.bind(addr)
tcpServerSocket.listen()
print('Server port:9876')
print('正在等待客户端连接')
tcpClientSocket,addr = tcpServerSocket.accept()
print('客户端已经连接','addr','=',addr)
fullDataBytes = b''
while True:    
    data = tcpClientSocket.recv(bufferSize)
    fullDataBytes += data
    if len(data) < bufferSize:
        break;
print(fullDataBytes)
print(fullDataBytes.decode('ISO-8859-1'))
tcpClientSocket.close()
tcpServerSocket.close()
        
        