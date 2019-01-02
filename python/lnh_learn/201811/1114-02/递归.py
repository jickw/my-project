#-*-coding:utf-8-*-
"""
__title__ = ''
__author__ = 'wux'
__mtime__ = '2018/11/14'
"""

# 遍历树形结构
import os


filePath = "d:\python_learn\lnh_learn"


def readpath(path, n):
    it = os.listdir(path)  # 查看文件夹中的文件
    # print("__iter__" in dir(it))  # 可迭代对象
    # print("__next__" in dir(it))

    for el in it:
        if os.path.isdir(os.path.join(path, el)):  # 判断文件是文件夹还是文件
            print("\t" * n, el)
            readpath(os.path.join(path, el), n+1)
        else:
            print("\t"*n, el)  # 递归出口


readpath(filePath, 0)
