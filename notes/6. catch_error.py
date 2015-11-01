# -*- coding: UTF-8 -*- 

import urllib.request

req = urllib.request.Request('http://laispace.com')
try:
	res = urllib.request.urlopen(req)
	content = res.read().decode('utf8')
	print(content)
except urllib.error.HTTPError as error:
	print(error.code)









