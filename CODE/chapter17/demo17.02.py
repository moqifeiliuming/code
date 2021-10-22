import _thread as thread
from time import sleep, ctime

def fun1():
 
    print('开始运行fun1:', ctime())
    sleep(4)
    print('fun1运行结束:', ctime())

def fun2():
    print('开始运行fun2:', ctime())
    sleep(2)
    print('fun2运行结束:', ctime())

def main():
    print('开始运行时间:', ctime())
    thread.start_new_thread(fun1, ())
    thread.start_new_thread(fun2, ())
    sleep(6)
    print('结束运行时间:', ctime())

if __name__ == '__main__':
    main()
