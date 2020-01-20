"""
500G 数据读取 特殊 只有1行 数据以{|}分割
生成器用于读取大文件
"""


def myreadlines(f, split_tag):
    buf = ""
    while True:
        while split_tag in buf:
            pos = buf.index(split_tag)
            yield buf[:pos]
            buf = buf[pos + len(split_tag):]
        chunk = f.read(4096 * 10)
        if not chunk:
            # 读至结尾
            yield buf
            break
        buf += chunk


with open("test.txt") as f:
    for line in myreadlines(f, "{|}"):
        print(line)
