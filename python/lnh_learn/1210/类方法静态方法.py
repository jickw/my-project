#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# class A:
#     def func(self):
#         print(self)
#
#     @classmethod
#     def func1(cls):
#         print(cls)


# A.func1()
# 类方法，通过类名调用的方法，类方法中的第一个参数约定俗成称cls，python自动将类名（空间）传给cls

# a1 = A()
# a1.func1() # 对象调用类方法，cls传的是类本身
# 类方法应用场景：
# 1、类中 有些方法是不需要对象参与
# class A:
#     name = 'alex'
#     count = 1
#
#     @classmethod
#     def func1(cls): # 此方法无需对象参与
#         return cls.name + str(cls.count+1)
#
# print(A.func1())
# 2、对类中的静态变量进行改变，要用类方法
# 3、继承中，父类得到子类的类空间

# class A:
#     name = 'alex'
#     count = 1
#
#     @classmethod
#     def func1(cls): # 此方法无需对象参与
#         # 对B类的内容可以进行修改
#         print(cls)
#         print(cls.age)
#
# class B(A):
#     age = 22
#     pass
#
# B.func1()
# 不通过类方法，通过父类的某个方法得到子类的类空间的所有值
# class A:
#     name = 'alex'
#     count = 1
#
#     def func2(self):
#         print(self)
#         print(self.age)
#
# class B(A):
#     age = 22
#
# b1 = B()
# b1.func2()
# 静态方法

class A:
    @staticmethod
    def login(username, passwd):
        if username == 'alex' and passwd == '1234':
            print('登录成功')
        else:
            print('登录失败')


A.login('alex', '1234')
# 1、代码块清晰
# 2、复用性

