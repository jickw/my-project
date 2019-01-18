#-*-coding:utf-8-*-
"""
__title__ = ''
__author__ = 'wux'
__mtime__ = '2019/1/16'
"""

import time

print(time.time())
print(time.strftime('%Y-%m-%d'))
time_obj = time.localtime()
print(time_obj.tm_year)
print(time_obj.tm_mday)