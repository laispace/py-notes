# -*- coding: UTF-8 -*- 

import urllib.request

enable_proxy = False
proxy_handler = urllib.request.ProxyHandler({
	'http': 'http://127.0.0.1"8080'
	})
null_proxy_handler = urllib.request.ProxyHandler({})

if (enable_proxy):
	opener = urllib.request.build_opener(proxy_handler)
else:
	opener = urllib.request.build_opener(null_proxy_handler)

urllib.request.install_opener(opener)

# 下载一个网页
url = 'http://www.meizi.us/'
f = opener.open(url)
print(content)








