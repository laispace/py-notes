# -*- coding: UTF-8 -*- 

import urllib.request


# 下载一个网页到本地
import urllib
url = 'http://www.laispace.com/'
filename = './download/laisace.com.html'
def callback(num, size, total):
	# num 已经下载好的数据块
	# size 每个数据块的大小
	# total 远程文件的大小
	percentage = 100.0 * num * size / total
	if percentage > 100:
		percentage = 100
	print('%.2f%%'%percentage )
urllib.request.urlretrieve(url, filename, callback)