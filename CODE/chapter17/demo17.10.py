from atexit import register
from random import randrange
from threading import BoundedSemaphore, Lock, Thread
from time import sleep, ctime

lock = Lock()
MAX = 5
candytray = BoundedSemaphore(MAX)

def refill():
    lock.acquire()
    print('重新添加糖果...', end=' ')
    try:
        candytray.release()
    except ValueError:
        print('糖果机都满了，无法添加')
    else:
        print('成功添加糖果')
    lock.release()

def buy():
    lock.acquire()
    print('购买糖果...', end=' ')
    if candytray.acquire(False):
        print('成功购买糖果')
    else:
        print('糖果机为空，无法购买糖果')
    lock.release()

def producer(loops):
    for i in range(loops):
        refill()
        sleep(randrange(3))

def consumer(loops):
    for i in range(loops):
        buy()
        sleep(randrange(3))

def main():
    print('开始:', ctime())
    nloops = randrange(2, 6)
    print('糖果机共有%d个槽!' % MAX)
    Thread(target=consumer, args=(randrange(
        nloops, nloops+MAX+2),)).start() 
    Thread(target=producer, args=(nloops,)).start() 

@register
def exit():
    print('程序执行完毕：', ctime())

if __name__ == '__main__':
    main()

