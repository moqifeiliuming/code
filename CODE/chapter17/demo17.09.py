from threading import BoundedSemaphore

MAX = 3
semaphore = BoundedSemaphore(MAX)
print(semaphore._value)
semaphore.acquire()
print(semaphore._value)
semaphore.acquire()
print(semaphore._value)
semaphore.acquire()
print(semaphore._value)
print(semaphore.acquire(False))

print(semaphore._value)
semaphore.release()
print(semaphore._value)
semaphore.release()
print(semaphore._value)
semaphore.release()
print(semaphore._value)
semaphore.release()


