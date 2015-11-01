# -*- coding: UTF-8 -*-

import urllib.request
import datetime
import time
from threading import Thread


class ThreadClass(Thread):
    def run(self):
        name = self.getName()
        now = datetime.datetime.now()
        print('%s 开始执行 %s' % (name, now))


for i in range(10):
    t = ThreadClass()
    t.start()
