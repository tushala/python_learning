import threading

# 条件变量 condition， 用于复杂的线程间同步 没有condition则顺序执行不会交叉执行
# class XiaoAi(threading.Thread):
#     def __init__(self, lock:threading.RLock):
#         super(XiaoAi, self).__init__(name="小爱")
#         self.lock = lock
#
#     def run(self):
#         self.lock.acquire()
#         print(f"{self.name}: 在")
#         self.lock.release()
#
#         self.lock.acquire()
#         print(f"{self.name}: 好啊")
#         self.lock.release()
#
# class TianMao(threading.Thread):
#     def __init__(self, lock:threading.RLock):
#         super().__init__(name="天猫精灵")
#         self.lock = lock
#
#     def run(self):
#
#         self.lock.acquire()
#         print("{} : 小爱同学 ".format(self.name))
#         self.lock.release()
#
#         self.lock.acquire()
#         print("{} : 我们来对古诗吧 ".format(self.name))
#         self.lock.release()

class XiaoAi(threading.Thread):
    def __init__(self, cond:threading.Condition):
        super(XiaoAi, self).__init__(name="小爱")
        self.cond = cond


    def run(self):
        with self.cond:
            self.cond.wait()
            print(f"{self.name}: 在")
            self.cond.notify()

            self.cond.wait()
            print(f"{self.name}: 好啊 ")
            self.cond.notify()

            self.cond.wait()
            print(f"{self.name}: 君住长江尾 ")
            self.cond.notify()


class TianMao(threading.Thread):
    def __init__(self, cond: threading.Condition):
        super(TianMao, self).__init__(name="天猫精灵")
        self.cond = cond

    def run(self):
        with self.cond:

            print(f"{self.name}: 小爱同学")
            self.cond.notify()
            self.cond.wait()

            print(f"{self.name}: 我们来对古诗吧 ")
            self.cond.notify()
            self.cond.wait()

            print(f"{self.name}: 我住长江头 ")
            self.cond.notify()
            self.cond.wait()


if __name__ == '__main__':
    # xiaoai = XiaoAi(threading.RLock())
    # tianmao = TianMao(threading.RLock())
    cond = threading.Condition()
    xiaoai = XiaoAi(cond)
    tianmao = TianMao(cond)

    xiaoai.start()
    tianmao.start()
