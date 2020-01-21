import time
import threading


def get_detail_html(url):
    print("get detail html started")
    time.sleep(2)
    print("get detail html end")


def get_detail_url(url):
    print("get detail url started")
    time.sleep(2)
    print("get detail url end")


# if __name__ == '__main__':
#     thread1 = threading.Thread(target=get_detail_html, args=("",))
#     thread2 = threading.Thread(target=get_detail_url, args=("",))
#     start = time.time()
#     thread1.start()
#     thread2.start()
#     print(time.time() - start)

# 通过继承Thread

class GetDetailHtml(threading.Thread):
    def __init__(self, name):
        super(GetDetailHtml, self).__init__(name=name)

    def run(self):
        print("get detail html started")
        time.sleep(2)
        print("get detail html end")


class GetDetailUrl(threading.Thread):
    def __init__(self, name):
        super(GetDetailUrl, self).__init__(name=name)

    def run(self):
        print("get detail url started")
        time.sleep(2)
        print("get detail url end")


if __name__ == '__main__':
    thread1 = GetDetailHtml("get_detail_html")
    thread2 = GetDetailUrl("get_detail_url")
    thread1.run()
    thread2.run()
    # thread1.join()
    # thread1.setDaemon(True)