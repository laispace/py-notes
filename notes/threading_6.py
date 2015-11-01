# -*- coding: UTF-8 -*-

import urllib.request
import time
import queue
import threading
from bs4 import BeautifulSoup

urls = [
    "http://alloyteam.com",
    "http://fex.baidu.com",
    "http://ued.taobao.org/",
    "http://www.75team.com/"
]

q = queue.Queue()
q2 = queue.Queue()


class ThreadUrl(threading.Thread):
    def __init__(self, q, q2):
        threading.Thread.__init__(self)
        self.q = q
        self.q2 = q2

    def run(self):
        while True:
            # 获取数据
            url = self.q.get()

            # 抓去网页
            res = urllib.request.urlopen(url)
            code = res.getcode()
            print(code, url)

            # 放入另一个队列
            chunk = res.read()
            self.q2.put(chunk)

            # 执行完毕
            # 一个任务执行完毕，任务数量减一，当数量减少到零时，解锁退出
            self.q.task_done()


class DatamineThread(threading.Thread):
    def __init__(self, q2):
        threading.Thread.__init__(self)
        self.q2 = q2

    def run(self):
        while True:
            chunk = self.q2.get()

            soup = BeautifulSoup(chunk, 'html.parser')
            print(soup.findAll(['title']))

            self.q2.task_done()


start = time.time()


def main():
    # 控制线程池数量
    for i in range(4):
        t = ThreadUrl(q, q2)
        t.setDaemon(True)
        t.start()

    # 提供数据给 queue
    for url in urls:
        q.put(url)

    # 控制线程池数量
    for i in range(4):
        t = DatamineThread(q2)
        t.setDaemon(True)
        t.start()

    # 将线程串联起来，当所有任务都执行时，才退出程序
    # join 也可以理解为加锁操作，记住任务数量
    q.join()
    q2.join()


main()

end = time.time()
print('耗时', end - start)
