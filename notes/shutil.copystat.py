# -*- coding: UTF-8 -*-

import os
import shutil


# 复制权限、最后访问时间、最后修改时间

src = '../data/shutil/srcmode.txt'
dst = '../data/shutil/dstmode.txt'

# 先设置两个文件权限不一样
os.system('chmod 777 ' + src)
os.system('chmod 644 ' + dst)
# 碰一下 src 设置修改时间
os.system('touch ' + src)
print('\n复制前：')
os.system('ls -l ' + src)
os.system('ls -l ' + dst)

# 复制权限
shutil.copystat(src, dst)

print('\n复制后：')
os.system('ls -l ' + src)
os.system('ls -l ' + dst)