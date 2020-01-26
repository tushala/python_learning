# Semaphore 是用于控制进入数量的锁
# ps.文件， 读、写， 写一般只是用于一个线程写，读可以允许有多个

import threading
import time


class HtmlSpider(threading.Thread):
    def __init__(self, url, sem: threading.Semaphore):
        super(HtmlSpider, self).__init__()
        self.url = url
        self.sem = sem

    def run(self):
        time.sleep(2)
        print("got html text success")
        self.sem.release()


class UrlProducer(threading.Thread):
    def __init__(self, sem: threading.Semaphore):
        super(UrlProducer, self).__init__()
        self.sem = sem

    def run(self):
        for i in range(20):
            self.sem.acquire()
            html_thread = HtmlSpider(f"https://baidu.com/news/{i}", self.sem)
            html_thread.start()


if __name__ == '__main__':
    sem = threading.Semaphore(3)
    url_producer = UrlProducer(sem)
    url_producer.start()