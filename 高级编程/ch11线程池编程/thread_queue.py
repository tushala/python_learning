"""
模拟爬虫 不推荐共享数据
"""
import threading
import time

# from xxx import xx的坑： 在xx修改后,本import无效
detail_url_list = []


def get_detail_html(detail_url_list):
    # 爬取文章详细页面
    # global detail_url_list
    while True:
        if len(detail_url_list) > 0:
            url = detail_url_list.pop()
            print(f"开始爬取{url}页面")
            time.sleep(0.5)  # 模拟爬取详细页面
            print(f"已爬取{url}页面")


def get_detail_url(detail_url_list):
    # 爬取文章列表详细页面
    # global detail_url_list
    print("开始爬取文章列表详细页面")
    time.sleep(2)
    for i in range(1, 21):
        detail_url_list.append(f"http://tushala.com/{i}")
    print("已爬取文章列表详细页面")


if __name__ == '__main__':
    thread_detail_url = threading.Thread(target=get_detail_url, args=(detail_url_list))
    for i in range(5):
        html_thread = threading.Thread(target=get_detail_html, args=(detail_url_list))
        html_thread.start()
    start_time = time.time()
