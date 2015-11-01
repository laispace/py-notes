# -*- coding: UTF-8 -*-

import shutil

# 复制文件，包括访问时间和修改时间
olddir = '../data/shutil/copy'
newdir = '../data/shutil/copy3'
newdir2 = '../data/shutil/copy4'

# 复制目录时将保持文件夹下的符号连接
shutil.copytree(olddir, newdir, True)

# 复制的目录下生成物理副本来替代符号连接
shutil.copytree(olddir, newdir2, False)
