from socket import *
host = ''
bufferSize = 1024
port = 9876
addr = (host,port)
tcpServerSocket = socket(AF_INET, SOCK_STREAM)
tcpServerSocket.bind(addr)
tcpServerSocket.listen()
print('Server port:9876')
print('正在等待客户端连接')
tcpClientSocket,addr = tcpServerSocket.accept()
print('客户端已经连接','addr','=',addr)
data = tcpClientSocket.recv(bufferSize)
print(data.decode('utf8'))
tcpClientSocket.send('你好，I love you.\n'.encode(encoding='utf_8'))
tcpClientSocket.close()
tcpServerSocket.close()
        
        