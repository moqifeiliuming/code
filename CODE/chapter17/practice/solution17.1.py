import _thread as thread
from time import sleep, ctime
import random
from threading import currentThread
def fun():
    for i in range(10):
        print(currentThread().name,i)
        sleep(random.randint(1,5))
def main():
    thread.start_new_thread(fun, ())
    thread.start_new_thread(fun, ())
    input()
if __name__ == '__main__':
    main()
