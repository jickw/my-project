#-*-coding:utf-8-*-
"""
__title__ = ''
__author__ = 'wux'
__mtime__ = '2019/1/2'
"""

'''
1、找到这个my_module模块
2、创建一个属于my_module的内存空间
3、执行my_module
4、将这个模块所在的命名空间建立一个和my_module之间的引用关系

导入多个模块
PEP8规范
所有的模块导入都应该尽量放在这个文件的开头
模块的导入也是有顺序的
先导入内置的模块
再导入第三方模块
最后导入自定义模块
'''

import my_module  # 要导入一个文件的名字，但是不加.py后缀名
# 模块的名字必须要满足变量的命名规范
# 一般情况下，模块都是小写字母开头的名字


# import这个语句相当于执行了这个模块所在的py文件

# 模块可以被多次导入么？一个模块不会被重复导入

# 如何使用模块
my_module.login()

print(my_module.name)

def login():
    print('in mine login!')

my_module.login()
login()
# 在导入一个模块的过程中到底发生了哪些事情

