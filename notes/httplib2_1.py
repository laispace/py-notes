# -*- encoding: utf-8 -*-
# https://github.com/jcgregorio/httplib2
# https://github.com/jcgregorio/httplib2/wiki/Examples-Python3

# 打开 http 的调试功能
from http.client import HTTPConnection
HTTPConnection.debuglevel = 1
from urllib.request import urlopen
response = urlopen('http://laispace.com')

print(response.headers.as_string())