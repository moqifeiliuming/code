import threading
from time import sleep, ctime

class MyThread(object):
    def __init__(self, func, args):
        self.func = func
        self.args = args

    def __call__(self):
        self.func(*self.args)
def fun(index, sec):
    print('开始执行', index, ' 时间:', ctime())
    sleep(sec)
    print('结束执行', index, '时间:', ctime())
def main():
    print('执行开始时间:', ctime())
    thread1 = threading.Thread(target = MyThread(fun,(10, 4)))
    thread1.start()
    thread2 = threading.Thread(target = MyThread(fun,(20, 2)))
    thread2.start()
    thread3 = threading.Thread(target = MyThread(fun,(30, 1)))
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()
    print('所有的线程函数已经执行完毕:', ctime())
if __name__ == '__main__':
    main()
