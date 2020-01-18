"""描述符使用"""
import numbers


class IntField:
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral) or value < 0:
            raise ValueError
        self.value = value

    def __delete__(self, instance):
        pass


class NotDataField:
    def __get__(self, instance, owner):
        return instance


class User:
    # age = IntField()
    # age = 100
    age = NotDataField()

    def __init__(self):
        # self.age = 765
        pass


if __name__ == '__main__':
    user = User()

    user.age = 1234
    print(user.__dict__)
    print(user.age)
    print(getattr(user, "age"))

"""
user.age 或者 getattr(user, "age")的执行顺序
如果user是某个类的实例：
首先调用__getattribute__ 再进入__getattr__

对于描述符(__get__)的调用，则发生在__getattribute__内部。
# user = User() user.age 或者 getattr(user, "age")的执行顺序为：
1.如果“age”在User或者 基类的__dict__切age是数据描述符，则调用其__get__
2.如果“age”在user的__dict__中,则返回user.__dict__["age"]
3.如果“age”在User或基类的__dict__中 返回User.__dict__["age"]
user.__dict__["age"] 不一定和 user.age相等
"""
