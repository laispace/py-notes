# -*- coding: UTF-8 -*-

import urllib.request
import time
import queue
import threading

urls = [
    "http://alloyteam.com",
    "http://fex.baidu.com",
    "http://ued.taobao.org/",
    "http://www.75team.com/"
]

q = queue.Queue()


class ThreadUrl(threading.Thread):
    """Threaded Url Grab"""

    def __init__(self, q):
        threading.Thread.__init__(self)
        self.q = q

    def run(self):
        while True:
            # 获取数据
            url = self.q.get()

            # 抓去网页
            res = urllib.request.urlopen(url)
            code = res.getcode()
            print(code, url)

            # 执行完毕
            # 一个任务执行完毕，任务数量减一，当数量减少到零时，解锁退出
            self.q.task_done()


start = time.time()


def main():
    # 控制线程池数量
    for i in range(4):
        t = ThreadUrl(q)
        t.setDaemon(True)
        t.start()

    # 提供数据给 queue
    for url in urls:
        q.put(url)

    # 将线程串联起来，当所有任务都执行时，才退出程序
    # join 也可以理解为加锁操作，记住任务数量
    q.join()

main()

end = time.time()
print('耗时', end - start)
