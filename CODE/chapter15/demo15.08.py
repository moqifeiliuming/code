from socket import *
host = 'localhost'
port = 9876
bufferSize = 1024
addr = (host, port)
udpClientSocket = socket(AF_INET, SOCK_DGRAM)
while True:
    data = input('>')
    if not data:
        break
    udpClientSocket.sendto(data.encode(encoding='utf-8'),addr)
    data,addr = udpClientSocket.recvfrom(bufferSize)
    if not data:
        break
    print(data.decode('utf-8'))
udpClientSocket.close()
    
    