#-*-coding:utf-8-*-
"""
__title__ = ''
__author__ = 'wux'
__mtime__ = '2018/12/15'
"""

# __名字__
# 类中的特殊方法\内置方法
# 双下方法
# 魔术方法  magic method
# 类中的每一个双下方法都有它自己的特殊意义


# __call__  flask
# __new__  特别重要
# 写一个单例类

# __len__
# __str__/__repr__

#
# class A:
#     def __call__(self, *args, **kwargs):
#         print('执行call方法')
#
#
# class B:
#     def __init__(self, cls):
#         self.a = cls()
#         self.a()

# a = A()
# a()  # 相当于调用__call__方法

# A()()# 和上面的结果一样，相当于调用__call__方法

#A()()   类名()()  相当于先实例化得到一个对象，再对对象(),==>和上面的结果一样，相当于调用__call__方法

# B(A)

# class mylist:
#     def __init__(self):
#         self.lst = [1,2,3,4,5,6]
#
#     def __len__(self):
#         print('执行了__len__')
#         return len(self.__dict__)
#
# l = mylist()
# print(len(l))
# len(obj)相当于调用了这个obj的__len__方法
# __len__方法return的值就是len函数的返回值
# 如果一个obj对象没有__len__方法，那么len函数会报错
#__len__
# 内置函数和内置方法是有关系的

# class My:
#     def __init__(self, s):
#         self.s = s
#
#     def __len__(self):
#         return len(self.s)
#
# my = My('aaaaaa')
# print(len(my))


# __new__  #==>构造方法
# __init__ #==>初始化方法

class Single:
    def __new__(cls, *args, **kwargs):
        print('创建一个对象')
        return object.__new__(cls)

    def __init__(self):
        print('init')

# 1. 开辟一个空间，属于对象的
# 2. 把对象的空间传给self，执行init
# 3. 将这个对象的空间返回给调用者

obj = Single()