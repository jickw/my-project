#-*-coding:utf-8-*-
"""
__title__ = ''
__author__ = 'wux'
__mtime__ = '2019/1/16'
"""

import sys

print(sys.argv)

name = sys.argv[1]
pwd = sys.argv[2]

if name == 'alex' and pwd == 'alex333':
    print('Hi alex')
else:
    print('fk u')
    exit(1)
