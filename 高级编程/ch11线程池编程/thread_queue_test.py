"""
Queue用法
"""
from queue import Queue
import time
import threading


def get_detail_html(queue):
    # 爬取文章详情页
    while True:
        url = queue.get()
        # for url in detail_url_list:
        print("get detail html started")
        time.sleep(2)
        print("get detail html end")


def get_detail_url(queue):
    # 爬取文章列表页
    while True:
        print("get detail url started")
        time.sleep(4)
        for i in range(20):
            queue.put("http://projectsedu.com/{id}".format(id=i))
        print("get detail url end")


if __name__ == '__main__':
    detail_url_queue = Queue(maxsize=1000)

    thread_detail_url = threading.Thread(target=get_detail_url, args=(detail_url_queue,))
    for i in range(10):
        html_thread = threading.Thread(target=get_detail_html, args=(detail_url_queue,))
        html_thread.start()

    start_time = time.time()
    detail_url_queue.task_done()
    detail_url_queue.join()
    print(f"last time: {time.time() - start_time)}")
