# -*- coding: UTF-8 -*-

import os
import shutil


# 复制文件权限,注意只会复制其权限
# 复制权限、最后访问时间、最后修改时间，则使用 copystat( src, dst)

src = '../data/shutil/srcmode.txt'
dst = '../data/shutil/dstmode.txt'

# 先设置两个文件权限不一样

os.system('chmod 777 ' + src)
os.system('chmod 644 ' + dst)
print('\n复制前：')
os.system('ls -l ' + src)
os.system('ls -l ' + dst)

# 复制权限
shutil.copymode(src, dst)

print('\n复制后：')
os.system('ls -l ' + src)
os.system('ls -l ' + dst)