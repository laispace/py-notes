# -*- coding: UTF-8 -*- 

import urllib.request

httpHandler = urllib.request.HTTPHandler(debuglevel=1)

httpsHandler = urllib.request.HTTPSHandler(debuglevel=1)

opener = urllib.request.build_opener(httpHandler, httpsHandler)

urllib.request.install_opener(opener)

res = urllib.request.urlopen('http://laispace.com')
code = res.getcode()
print(code)













