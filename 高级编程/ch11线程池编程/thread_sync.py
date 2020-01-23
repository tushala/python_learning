from threading import Lock, RLock, Condition

# Rlock可重入的锁 允许多个acquire Lock多次acquire不release会导致死锁
#1. 用锁会影响性能
#2. 锁会引起死锁(Lock)

total = 0
lock = RLock()


def add():
    # 1. dosomething1
    # 2. io操作
    # 1. dosomething3
    global lock
    global total
    for i in range(1000000):
        lock.acquire()
        lock.acquire()
        total += 1
        lock.release()
        lock.release()


def desc():
    global lock
    global total
    for i in range(1000000):
        lock.acquire()
        total -= 1
        lock.release()


if __name__ == '__main__':
    import threading

    thread1 = threading.Thread(target=add)
    thread2 = threading.Thread(target=desc)
    thread1.start()
    thread2.start()

    #
    thread1.join()
    thread2.join()
    # from time import sleep
    # sleep(200)
    print(total)
