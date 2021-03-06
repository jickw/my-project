#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# 广义的封装  ： 实例化一个对象，给对象空间封装一些属性

# 狭义的封装：  私有制
# 私有成员 ： 私有静态字段， 私有方法， 私有对象属性

# 私有静态字段

# class B:
#     __money = 100000
#
#
# class A(B):
#     name = 'alex'
#     __age = 100
#     def func(self):
#         print(self.__age)
#         print(A.__age)
#         print('func...')
#     def func1(self):
#         print(self.__money)


# a1 = A()
# print(a1.name)
# print(A.name)
# print(a1.__age)  # 实例化对象不能访问私有静态字段

# print(A.__age) # 类名不能直接访问私有静态字段
# 对于私有静态字段，类的外部不能访问

# 对于私有静态字段，类的内部可以访问
# a1.func()

# 对于私有静态字段，只能在本类中内部访问，类的外部，派生类均不可访问
# a1.func1()

# 可以访问，但是工作中千万不能用

# print(a1._A__age)


class B:
    def __f1(self):
        print()


class A(B):
    name = 'alex'
    def __func(self):
        print('func...')

    def func1(self):
        # self.__func()  # 类的外部可以访问
        self.__f1()
a1 = A()
# a1.__func()  # 类的外部不可以访问
a1.func1()

