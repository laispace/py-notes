# -*- encoding: utf-8 -*-
# https://github.com/jcgregorio/httplib2
# https://github.com/jcgregorio/httplib2/wiki/Examples-Python3

import httplib2

httplib2.debuglevel = 1

# .cache 指定了缓存目录
h = httplib2.Http('.cache')

response, content = h.request('http://laispace.com')