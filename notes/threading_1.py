# -*- coding: UTF-8 -*-

import time
import urllib.request


def get_responses():
    urls = [
        "http://alloyteam.com",
        "http://fex.baidu.com",
        "http://ued.taobao.org/",
        "http://www.75team.com/"
    ]
    start = time.time()
    for url in urls:
        print(url)
        resp = urllib.request.urlopen(url)
        print(resp.getcode())
    print("耗时: %s" % (time.time() - start))


get_responses()
