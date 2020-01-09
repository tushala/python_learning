# try:
#     print("code started")
#     raise IndexError
# except KeyError as e:
#     print("Key Error")
# finally:
#     print("otrher error")

# finallly > except > try

# 上下文管理器协议
class Sample:
    def __enter__(self):
        # 获取资源
        print("enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 释放资源
        print("exit")

    def do_something(self):
        print("do_something")


if __name__ == '__main__':
    with Sample() as s:
        s.do_something()
