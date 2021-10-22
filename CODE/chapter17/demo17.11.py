from random import randrange
from time import sleep,time, ctime
from threading import Lock, Thread
from queue import Queue
lock = Lock()
class MyThread(Thread):
    def __init__(self, func, args):
        super().__init__(target = func, args = args)

def writeQ(queue):
    lock.acquire()
    print('生产了一个对象，并将其添加到队列中', end='  ')
    queue.put('商品')
    print("队列尺寸", queue.qsize())
    lock.release()

def readQ(queue):
    lock.acquire()
    val = queue.get(1)
    print('消费了一个对象，队列尺寸：', queue.qsize())
    lock.release()

def writer(queue, loops):
    for i in range(loops):
        writeQ(queue)
        sleep(randrange(1, 4))

def reader(queue, loops):
    for i in range(loops):
        readQ(queue)
        sleep(randrange(2, 6))

funcs = [writer, reader]
nfuncs = range(len(funcs))

def main():
    nloops = randrange(2, 6)
    q = Queue(32)

    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (q, nloops))
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()

    print('所有的工作完成')

if __name__ == '__main__':
    main()
