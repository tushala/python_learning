from collections import UserList

"""
list 中实现迭代原理 __iter__部分代码
"""


def __iter__(self):
    i = 0
    try:
        while True:
            v = self[i]
            yield v
            i += 1
    except IndexError:
        return
