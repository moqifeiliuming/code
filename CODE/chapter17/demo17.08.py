from atexit import register
import random
from threading import Thread, Lock, currentThread
from time import sleep, ctime

lock = Lock()
def fun():   
    lock.acquire()
    for i in range(5):
        print('Thread Name','=',currentThread().name,'i','=',i)
        sleep(random.randint(1,5))
    lock.release()
def main():
    for i in range(3):
        Thread(target=fun).start()
@register
def exit():
    print('线程执行完毕:', ctime())
if __name__ == '__main__':
    main()