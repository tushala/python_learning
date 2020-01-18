class User:
    def __new__(cls, name):
        print("in new")
        print(name[:2])
        return super().__new__(cls)
    def __init__(self, name):
        self.name = name

# new用来控制对象生成的过程, 在对象生成之前
# init用来完善对象
# 如果new不返回对象，则不会调用init函数
if __name__ == '__main__':
    user = User("tushala")