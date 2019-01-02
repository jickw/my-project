#-*-coding:utf-8-*-
"""
__title__ = ''
__author__ = 'wux'
__mtime__ = '2018/11/3'
"""
import os

with open('吃的', mode='r', encoding='utf-8') as f1, open('吃的_副本', mode='w', encoding='utf-8') as f2:
    s = f1.read()
    ss = s.replace("肉", "菜")
    f2.write(ss)

os.remove("吃的")   # 删除文件
os.rename("吃的_副本", "吃的")  # 重命名文件
