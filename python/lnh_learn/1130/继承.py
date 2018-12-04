#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# 面向对象三大特性： 继承，多态， 封装

# 继承初识

# class Animal:
#     breath = "呼吸"
#
#     def __init__(self, name, sex, age):
#         self.name = name
#         self.sex = sex
#         self.age = age
#
#     def eat(self):
#         print('吃东西')
#
#     def drink(self):
#         print('喝东西')
#
#
# class Cat(Animal):
#     def miaow(self):
#         print('喵喵喵')
#
#
# class Dog(Animal):
#     def bark(self):
#         print('汪汪汪')
#
#
# class Bird(Animal):
#     def __init__(self, name, sex, age, wing):
#         # Animal.__init__(self, name, sex, age)
#         super().__init__(name, sex, age)
#         self.wing = wing
#
#     def bark(self):
#         print('嗷嗷叫')
#
#     def eat(self):
#         Animal.eat(self)
#         # super().eat()
#         print('鸟吃虫')

# class Chook(Animal):  # 括号里面的  父类，基类， 超类  括号外面的 子类， 派生类
#     pass
# 只执行父类的方法： 子类中不要定义与父类同名的方法
# 只执行子类的方法： 在子类中创建这个方法
# 既要执行子类的方法，又要执行父类的方法
# 有两种解决方案：
# 1、Animal.__init__(self, name, sex, age)
# 2、super().__init__(name, sex, age)

#
# b1 = Bird('鹦鹉', '公', 10, '绿翅膀')
# b1.eat()

# 继承的进阶
# 继承：  单继承，多继承
# object
# 类： 经典类， 新式类
# 新式类： 凡是继承object类的都是新式类
# python3x所有的类都是新式类, 因为python3x中的类都默认继承object
# class A:
#     pass
# 经典类： 不继承object类都是经典类
# python2x:(既有新式类，又有经典类) 所有的类默认都不继承object，所有的类默认都是经典类，你可以让其继承object

# class A(object):
#     pass

# 单继承： 新式类，经典类查询顺序一样


# class A:
#     def func(self):
#         print('IN A')
#
#
# class B(A):
#     pass
#     # def func(self):
#     #     print('IN B')
#
#
# class C(B):
#     pass
#     # def func(self):
#     #     print('IN C')
#
#
# c1 = C()
# # c1.func()

# 多继承
# 新式类：遵循广度优先
# 广度优选： 每个节点有且只走一次
# 经典类：遵循深度优先

# 多继承的新式类

# class A:
#     def func(self):
#         print('IN A')
#
#
# class B(A):
#     pass
#     # def func(self):
#     #     print('IN B')
#
#
# class C(A):
#     pass
#     # def func(self):
#     #     print('IN C')
#
#
# class D(B):
#     pass
#     # def func(self):
#     #     print('IN D')
#
#
# class E(C):
#     pass
#     # def func(self):
#     #     print('IN E')
#
#
# class F(D, E):
#     pass
#     # def func(self):
#     #     print('IN F')
#
#
# f1 = F()
# f1.func()
# print(F.mro())  # 查询类的继承顺序

# 多继承
# 新式类：一条路走到倒数第二级，判断其他路能走到终点，则返回走另一条，如果不能，则走到终点

# 经典类：一条路走到底
class A:
    pass
    # def func(self):
    #     print('IN A')


class B(A):
    pass
    # def func(self):
    #     print('IN B')


class C(A):
    # pass
    def func(self):
        print('IN C')


class D(B):
    pass
    # def func(self):
    #     print('IN D')


class E(C):
    pass
    # def func(self):
    #     print('IN E')


class F(D, E):
    pass
    # def func(self):
    #     print('IN F')


f1 = F()
f1.func()

# print(F.mro())  # 查询类的继承顺序

# 继承的优点：
# 1、节省代码
# 2、规范代码
# 初识继承：
# 只执行本类的方法
# 只执行父类的方法
# 即执行本类又执行父类方法
# 父类名.方法名(参数)
# super().方法名(参数(self自动传值))

# 单继承，多继承
# 类：新式类，经典类
#
# 单继承：
#     新式类经典类一样
#
# 多继承：
#     新式类：广度优先  类名.mro()
#     经典类：深度优先



