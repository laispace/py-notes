# -*- coding: UTF-8 -*- 

import urllib.parse
import urllib.request

url = 'http://www.laispace.com/login'
values = {
	'username': 'laixiaolai@laispace.com',
	'password': 'pass4laixiaolai'
}


data = urllib.parse.urlencode(values).encode('utf-8')
req = urllib.request.Request(url, data)
req.add_header('Referer', 'http://www.laispace.com/')
req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36')
f = urllib.request.urlopen(req)
content = f.read().decode('utf-8')
print(content)








