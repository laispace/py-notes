# -*- coding: UTF-8 -*-

import shutil

# 复制文件，可为文件到文件或文件到目录
# 注意如果还需要复制访问时间和修改时间，则使用 copy2(src, dst)
src = '../data/shutil/src.txt'
dst = '../data/shutil/src.copy.txt'
dst2 = '../data/shutil/copy'
shutil.copy(src, dst)
shutil.copy(src, dst2)