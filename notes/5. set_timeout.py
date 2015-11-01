# -*- coding: UTF-8 -*- 

import socket
import urllib.request

socket.setdefaulttimeout(1)

# 下载一个网页
url = 'http://www.laispace.com/'
f = urllib.request.urlopen(url)
content = f.read().decode('utf-8');
print(content)










