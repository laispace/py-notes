# -*- coding: UTF-8 -*-

import shutil

# 复制文件, 注意是文件到文件
# dst 必须是完整的目标文件名
# dst 必须可写, 否则抛出 IOException
# dst 如果已经存在则会被覆盖
src = '../data/shutil/src.txt'
dst = '../data/shutil/src.copy.txt'
shutil.copyfile(src, dst)