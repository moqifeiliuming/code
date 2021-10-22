from socket import *
host = ''
port = 9999
bufferSize = 1024
addr = (host, port)
udpServerSocket = socket(AF_INET, SOCK_DGRAM)
udpServerSocket.bind(addr)
while True:
    print('正在等待消息......')
    try:
        data, addr = udpServerSocket.recvfrom(bufferSize)
        pythonCode = data.decode('utf-8')
        print(pythonCode)
        result = eval(pythonCode)
        udpServerSocket.sendto(str(result).encode(encoding='utf-8'),addr)
        print('客户端地址：',addr)
    except Exception as e:
        print(e)
udpServerSocket.close()