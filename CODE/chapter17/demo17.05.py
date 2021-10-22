import threading
from time import sleep, ctime
def fun(index, sec):
    print('开始执行', index, ' 时间:', ctime())
    sleep(sec)
    print('结束执行', index, '时间:', ctime())
def main():
    thread1 = threading.Thread(target=fun,
            args=(10, 4))
    thread1.start()
    thread2 = threading.Thread(target=fun,
            args=(20, 2))
    thread2.start()
    thread1.join()
    thread2.join()

if __name__ == '__main__':
    main()
