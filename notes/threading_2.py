# -*- coding: UTF-8 -*-

import urllib.request
import time
from threading import Thread


class GetUrlThread(Thread):
    def __init__(self, url):
        self.url = url
        super(GetUrlThread, self).__init__()

    def run(self):
        resp = urllib.request.urlopen(self.url)
        print(self.url, resp.getcode())


def get_responses():
    urls = [
        "http://alloyteam.com",
        "http://fex.baidu.com",
        "http://ued.taobao.org/",
        "http://www.75team.com/"
    ]
    start = time.time()
    threads = []
    for url in urls:
        t = GetUrlThread(url)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print("耗时: %s" % (time.time() - start))


get_responses()
