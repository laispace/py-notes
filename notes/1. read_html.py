# -*- coding: UTF-8 -*- 

import urllib.request

# 下载一个网页
url = 'http://www.meizi.us/'
f = urllib.request.urlopen(url)
# 响应头
info = f.info()
# 响应体
content = f.read().decode('utf-8');
# 状态码
code = f.getcode()
# 请求 url
url = f.geturl()

print(code, url, info)


