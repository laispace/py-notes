# -*- coding: UTF-8 -*-

import urllib.request
import datetime
import time
from threading import Thread

urls = [
    "http://alloyteam.com",
    "http://fex.baidu.com",
    "http://ued.taobao.org/",
    "http://www.75team.com/"
]

start = time.time()
for url in urls:
    res = urllib.request.urlopen(url)
    code = res.getcode()
    print(code, url)
end = time.time()
print('耗时', end - start)
