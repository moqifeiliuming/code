import _thread as thread
from time import sleep, ctime
def fun(index, sec,lock):
    print('开始执行', index,'执行时间：',ctime())
    sleep(sec)
    print('执行结束',index,'执行时间：',ctime())
    lock.release()

def main():
    lock1 = thread.allocate_lock()
    lock1.acquire()
    thread.start_new_thread(fun, 
            (10, 4, lock1))
    lock2 = thread.allocate_lock()
    lock2.acquire()
    thread.start_new_thread(fun, 
            (20, 2, lock2))
    while lock1.locked() or lock2.locked():
        pass    
if __name__ == '__main__':
    main()
