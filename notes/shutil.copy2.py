# -*- coding: UTF-8 -*-

import shutil

# 复制文件，包括访问时间和修改时间
src = '../data/shutil/src.txt'
dst = '../data/shutil/copy2/src.copy.txt'
dst2 = '../data/shutil/copy2'
shutil.copy(src, dst)
shutil.copy(src, dst2)