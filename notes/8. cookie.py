# -*- coding: UTF-8 -*- 

import urllib.request

import http.cookiejar

cookie = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))

response = opener.open('http://www.baidu.com')
for item in cookie:
    print('%s = %s'%(item.name,item.value))













