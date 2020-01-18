"""__getattr__ 和__getattribute__"""

# 优先进入__getattribute__ 再进入__getattr__不建议修改__getattribute__
class User:
    def __init__(self, info):
        self.info = info

    def __getattr__(self, item):
        return self.info[item]

    def __getattribute__(self, item):

        return "abc"
        # return f"没有{item}特性"


if __name__ == '__main__':
    user = User(info={"name": "tushala", "height": "175cm", "gender": "male"})
    print(user.name)
    print(user.gender)
    print(user.height)
    print(user.weight)
