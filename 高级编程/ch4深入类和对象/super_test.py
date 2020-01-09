class A:
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        print("B")
        super(B, self).__init__()


class C(A):
    def __init__(self):
        print("C")
        super(C, self).__init__()


class D(B, C):
    def __init__(self):
        print("D")
        super(D, self).__init__()


if __name__ == '__main__':
    print(D.__mro__)
    d = D()