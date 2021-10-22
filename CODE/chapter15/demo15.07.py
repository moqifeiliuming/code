from socket import *
from time import ctime
host = ''
port = 9876
bufferSize = 1024
addr = (host, port)
udpServerSocket = socket(AF_INET, SOCK_DGRAM)
udpServerSocket.bind(addr)
while True:
    print('正在等待消息......')
    data, addr = udpServerSocket.recvfrom(bufferSize)
    udpServerSocket.sendto(ctime().encode(encoding='utf-8') + b' ' + data,addr)
    print('客户端地址：',addr)
udpServerSocket.close()