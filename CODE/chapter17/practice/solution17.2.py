import _thread as thread
from time import sleep, ctime
import random
from threading import Lock,currentThread
lock = Lock()
def fun():
    lock.acquire()
    for i in range(10):
        print(currentThread().name,i)
        sleep(random.randint(1,5))
    lock.release()
def main():
    thread.start_new_thread(fun, ())
    thread.start_new_thread(fun, ())
    input()
if __name__ == '__main__':
    main()
