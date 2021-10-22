from socket import *
host = 'localhost'
port = 9876
bufferSize = 1024
addr = (host, port)
while True:
    tcpClientSocket = socket(AF_INET, SOCK_STREAM)
    tcpClientSocket.connect(addr)
    data = input('>')
    if not data:
        break
    tcpClientSocket.send(('%s\r\n' % data).encode(encoding='utf-8'))
    data = tcpClientSocket.recv(bufferSize)
    if not data:
        break
    print(data.decode('utf-8').strip())
    tcpClientSocket.close()
    