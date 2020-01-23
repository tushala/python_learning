import threading
import time


def thread_job():
    # print("This is added Thread")
    print("T1 start\n")
    for i in range(10):
        time.sleep(0.1)
    print("T1 finish\n")


def T2_job():
    print("T2 start\n")
    print("T2 end\n")


def main():
    added_thread = threading.Thread(target=thread_job, name="T1")
    thread2 = threading.Thread(target=T2_job, name="T2")
    # print(threading.active_count())  # 线程激活数
    # print(threading.enumerate())  # 线程详细信息
    # print(threading.current_thread())  # 当前正在运行的线程
    added_thread.start()
    thread2.start()
    added_thread.join()  # 当前线程运行完后再往下运行
    thread2.join()
    print("all done")


def run():
    time.sleep(2)
    print('当前线程的名字是： ', threading.current_thread().name)
    time.sleep(2)


if __name__ == '__main__':
    # main()
    start_time = time.time()
    print('这是主线程：', threading.current_thread().name)
    thread_list = []
    for i in range(5):
        t = threading.Thread(target=run)
        thread_list.append(t)

    for t in thread_list:
        t.setDaemon(True) # 设置子守护线程
        # 设置子线程为守护线程时，主线程一旦执行结束，则全部线程全部被终止执行，
        # 可能出现的情况就是，子线程的任务还没有完全执行结束，就被迫停
        # 在start()之前主线程结束以后，子线程还没有来得及执行，整个程序就退出了
        t.start()
    for t in thread_list:
        t.join()
    # 可以看到，主线程一直等待全部的子线程结束之后，主线程自身才结束，程序退出
    # join所完成的工作就是线程同步，即主线程任务结束之后，进入阻塞状态，一直等待其他的子线程执行结束之后，主线程在终止
    # time.sleep(10)
    print('主线程结束！', threading.current_thread().name)
    print('一共用时：', time.time() - start_time)
