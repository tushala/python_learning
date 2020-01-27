# 多进程编程
# 对于io操作使用多线程， 进程切换代价高于线程
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from concurrent.futures import ProcessPoolExecutor


# 1.对于耗cpu的操作: 多进程优于多线程
def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


# if __name__ == '__main__':
#     # with ThreadPoolExecutor(3) as executor:  # 49.25
#     with ProcessPoolExecutor(3) as executor:   # 35.68
#         all_task = [executor.submit(fib, (num)) for num in range(25, 40)]
#         start_time = time.time()
#         for future in as_completed(all_task):
#             data = future.result()
#             print(f"exe result: {data}")
#         print("last time is: {}".format(time.time() - start_time))

# 2.对于io的操作: 多线程优于多进程
def random_sleep(n):
    time.sleep(n)
    return n


if __name__ == '__main__':
    with ThreadPoolExecutor(3) as executor:     # 20.01
    # with ProcessPoolExecutor(3) as executor:  # 20.75
        all_task = [executor.submit(random_sleep, (num)) for num in [2] * 30]
        start_time = time.time()
        for future in as_completed(all_task):
            data = future.result()
            print(f"exe result: {data}")

        print("last time is: {}".format(time.time() - start_time))
