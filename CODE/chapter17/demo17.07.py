
import threading
from time import sleep, ctime


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        super().__init__(target=func, name=name,
                 args=args)

    def run(self):
        self._target(*self._args)

def fun(index, sec):
    print('开始执行', index, '时间:', ctime())
    sleep(sec)
    print('执行完毕', index, '时间:', ctime())

def main():
    print('开始:', ctime())
    thread1 = MyThread(fun,(10,4),'线程1')
    thread2 = MyThread(fun,(20,2),'线程2')

    thread1.start()
    thread2.start()
    print(thread1.name)
    print(thread2.name)
    thread1.join()
    thread2.join()
    
    print('结束:', ctime())

if __name__ == '__main__':
    main()
