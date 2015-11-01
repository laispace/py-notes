# -*- coding: UTF-8 -*- 

import urllib.request

# 创建一个密码管理器
password_manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()

# 添加用户名和密码
url = 'http://laispace.com'
username = 'laixiaolai'
password = 'pass4laixiaolai'
password_manager.add_password(None, url, username, password)

# 创建一个 handler
handler = urllib.request.HTTPBasicAuthHandler(password_manager)

# 创建并安装一个 opener
opener = urllib.request.build_opener(handler)
urllib.request.install_opener(opener)

# 抓取网页（自带登录）
res = urllib.request.urlopen(url)
content = res.read().decode('utf8')
print(content)












