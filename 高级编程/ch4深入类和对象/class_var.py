class A:
    aa = 1

    def __init__(self, x, y):
        self.x = x
        self.y = y


a = A(2, 3)
print(a.__dict__)  # {'x': 2, 'y': 3}
A.aa = 11
a.aa = 100  # 在实例上添加属性
print(a.__dict__)  # {'x': 2, 'y': 3, 'aa': 100}
print(a.x, a.y, a.aa)
print(A.aa)
