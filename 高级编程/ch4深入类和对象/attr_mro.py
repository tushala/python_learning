"""类属性查找顺序"""


class AA:
    name = "a"

    def __init__(self):
        self.name = "b"


# a = AA()
# print(a.name)
# C3算法

# class D:
#     pass
#
#
# class C(D):
#     pass
#
#
# class B(D):
#     pass
#
#
# class A(B, C):
#     pass
#
#
# print(A.__mro__)
class E:
    pass


class D:
    pass


class C(E):
    pass


class B(D):
    pass


class A(B, C):
    pass


print(A.__mro__)
