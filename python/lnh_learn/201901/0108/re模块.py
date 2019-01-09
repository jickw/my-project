#-*-coding:utf-8-*-
"""
__title__ = ''
__author__ = 'wux'
__mtime__ = '2019/1/8'
"""

import  re

# ret = re.findall('\d', '392439fjdjfdkse883jfdj3fd')
# print(ret)
#
# ret2 = re.search('\d', '392439fjdjfdkse883jfdj3fd')
# print(ret2)

ret = re.sub('\d+', 'H', 'replace789nbc2xced389dcd')
print(ret)

ret2 = re.subn('\d+', 'H', 'replace789nbc2xced389dcd')
print(ret2)

