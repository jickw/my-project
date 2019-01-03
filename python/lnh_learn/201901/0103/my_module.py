#-*-coding:utf-8-*-
"""
__title__ = ''
__author__ = 'wux'
__mtime__ = '2019/1/2'
"""
__all__ = ['login', 'name']
print('饿了呢')

name = 'wux'

def login():
    print('这是一个登陆函数',name)


import sys

print(sys.modules['__main__'])

name = 'alex'
if __name__ == '__main__':
    print(__name__, type(__name__))
