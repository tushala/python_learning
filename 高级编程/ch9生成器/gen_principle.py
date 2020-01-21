"""生成器原理 网络摘抄 https://www.cnblogs.com/traditional/p/9221680.html"""
import dis  # 分析字节码


def gen_func():
    yield 123
    name = "satori"
    yield 456
    age = 18
    return "i love satori"


gen = gen_func()
# print(dis.dis(gen))
"""
  6           0 LOAD_CONST               1 (123)
              2 YIELD_VALUE
              4 POP_TOP

  7           6 LOAD_CONST               2 ('satori')
              8 STORE_FAST               0 (name)

  8          10 LOAD_CONST               3 (456)
             12 YIELD_VALUE
             14 POP_TOP

  9          16 LOAD_CONST               4 (18)
             18 STORE_FAST               1 (age)

 10          20 LOAD_CONST               5 ('i love satori')
             22 RETURN_VALUE
"""

print(gen.gi_frame.f_lasti)  # 记录了最近一次执行状态
print(gen.gi_frame.f_locals)  # 当前的局部变量
"""
-1
{}
"""
next(gen)
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)
"""
2
{}
"""
next(gen)
print(gen.gi_frame.f_lasti)   # 指向第十二行
print(gen.gi_frame.f_locals)  # 此时name="satori"，被添加到了局部变量当中
"""
12
{'name': 'satori'}
"""
next(gen)
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)  # StopIteration: i love satori

# 因为PyGenObject对函数的暂停和前进，进行了完美的监督，有变量保存我最近一行代码执行到什么位置
# 再通过yield来暂停它，就实现了我们的生成器

# 跟函数一样，我们的生成器对象也是分配在堆内存当中的，可以像函数的栈帧一样，独立于调用者而存在
# 我们可以在任何地方去调用它，只要我们拿到这个栈帧对象，就可以控制它继续往前走
# 正是因为可以在任何地方控制它，才会有了协程这个概念，这是协程能够实现的理论基础
# 因为有了f_lasti，生成器知道下次会在什么地方执行，不像函数，必须要一次性运行完毕
# 以上就是生成器的运行原理