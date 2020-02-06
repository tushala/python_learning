import multiprocessing
import time


def get_html(n):
    time.sleep(n)
    print("sub_progress success")
    return n


if __name__ == '__main__':
    # progress = multiprocessing.Process(target=get_html, args=(2,))
    # print(progress.pid)
    # progress.start()
    # print(progress.pid)
    # progress.join()
    # print("main progress end")

    # 使用线程池
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    # result = pool.apply_async(get_html, args=(3, ))
    #     #
    #     # # 等待所有任务完成
    #     # pool.close()
    #     # pool.join()
    #     #
    #     # print(result.get())  # 3

    # imap返回结果顺序和输入相同，imap_unordered则为不保证顺序
    # for result in pool.imap(get_html, [1, 5, 3]):
    #     print(f"{result} sleep success")

    for result in pool.imap_unordered(get_html, [1, 5, 3]):
        print("{} sleep success".format(result))
