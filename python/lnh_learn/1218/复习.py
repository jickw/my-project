#!/usr/bin/env python
# -*- encoding: utf-8 -*-


# 面向对象
# 写代码的时候  什么时候用面向对象
# 代码量大，功能多的时候
# 处理比较复杂的角色之间的关系
# 代码的清晰度提高
# 可读性  无论是开发者还是调用者，都能明确的分辨出每个角色拥有的方法和属性
# 增加了代码的可扩展性
# 增加复用性
# 增加规范


# python当中一切皆对象
# 基础数据类型  都是对象

# 类型和类的关系
# 类型和自定义类的关系   类型和类是一个东西

# 创建一个对象
# 类名() 实例化
# __new__() 创造了一个对象的空间，一些简单的初始化

# 创建一个类
# class 类名  语法级别的python解释器
# 类也是被创建出来的，type创建类
# class A(metaclass=ABCMeta)  ABCMeta创建了这个A类，那么ABCMeta就是A的元类
# 那么type就是这个类的元类

# type(obj)  的结果就是这个对象所属的类
# type(类) 的结果就是创建这个类的元类，大多数情况下是type，除非你指定metaclass

# from abc import ABCMeta
# class A(metaclass=ABCMeta):pass
#
# print(type(A))


# 类
# 类是什么时候被加载的，以及类名是什么时候产生的
# 类
#  静态属性/静态字段/静态变量
#  动态属性/方法
# class Person:
#     ROLE = 'CHINA'
#     print(ROLE)
#
#     def func(self):
#         pass
#         # print(ROLE)
#
# a = Person()
#
# print(Person.func)
# print(a.func)

# 对象
#  类创造对象的过程就是实例化的过程，构造new，初始化init
#  可以通过指针找到类的空间中的内容
#  对象本身也存储了一些只属于对象的属性

# 组合  什么有什么的关系
#  一个类的对象作为另一个类对象的属性

# 继承  什么是什么的关系  节省代码
#  单继承 和 多继承
#    单继承
#      如果子类的对象调用某个方法
#          子类有：调用子类的
#              子类有但想调用父类的
#                super  不用自己传self， super（子类，self）.方法名（除self之外的参数）
#                父类名 父类名.方法名（self，。。。）
#          子类没有：调用父类的
#      注意： 在任何类中调用的方法，都要自行分辨这个self是谁的对象
class Foo:
    def __init__(self):
        self.func()

    def func(self):print('Foo.func')

class Son(Foo):
    def func(self):print('Son.Foo')

s = Son()


#  子类  和  父类

#  经典类，新式类

# 封装
# 多态
# 鸭子类型
# property
# classmethod
# staticmethod
# 抽象类和接口类
# 反射
# 进阶
# 内置方法