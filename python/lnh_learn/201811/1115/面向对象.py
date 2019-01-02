#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# l1 = [1,2,3]
# count = 0
# for i in l1:
#     count += 1
# print(count)
#
# def my_len(argv):
#     count = 0
#     for i in argv:
#         count = count + 1
#     return count
#
# def add(name, sex, phone):
#     '''100行代码'''
#     pass
#
#
# def remove(name, sex, phone):
#     '''100行代码'''
#     pass
#
#
# def update(name, sex, phone):
#     '''100行代码'''
#     pass
#
#
# def find(name, sex, phone):
#     '''100行代码'''
#     pass


# 类： 具有相同属性的一类事物
# 人类：
# 对象：具体类的表现，具体的实实在在的一个实例
# 人事一类，大秧歌是一个对象
# 狗是一类，我家养的旺财是一个对象
#
#
# class Person:
#     '''类体： 两部分 ：变量部分，方法（函数）部分'''
#     mind = '思想'
#     animal = '高级动物'
#     faith = '信仰'
#
#     def __init__(self):
#         print(self)
#         print(666)
#
#     def work(self):
#         print('人类都会工作。。。')
#
#     def shopp(self):
#         print('人类可以消费')


# 类名的角度
# 操作类中的静态变量
# 1. Person.__dict__  查询类中的所有内容 （不能进行增删改操作）

# print(Person.__dict__)
# print(Person.__dict__['faith'])
# Person.__dict__['mind'] = '无脑'
# print(Person.__dict__['mind'])
# 2. 万能的. dot  对类中的单个的变量进行增删改查，用万能的 ‘.’

# print(Person.mind)
# print(Person.animal)  # 查

# Person.money = '运用货币'  # 增
# Person.mind = '无脑的'  # 改
# del Person.mind  # 删
# print(Person.__dict__)
# 操作类中的方法（基本不用类名去操作）
# print(Person.__dict__)
# Person.work(Person)
# 对象的角度
# ret = Person()  # 类名+() 过程： 实例化的过程(创建一个对象的过程)，实例化对象，实例， 对象。
# print(ret)
# # 1. 只要类名+() 产生一个对象，自动执行类中的__init__方法


class Person:
    '''类体： 两部分 ：变量部分，方法（函数）部分'''
    mind = '思想'
    animal = '高级动物'
    faith = '信仰'

    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby

    def work(self):
        print('%s会工作。。。' % self.name)

    def shopp(self):
        print('人类可以消费')


ret = Person('alex', 1000, 'women')  # 类名+() 过程： 实例化的过程(创建一个对象的过程)，实例化对象，实例， 对象。
# 1. 类名+() 产生一个实例（对象，对象空间）
# 2. 自动执行类中的__init__方法，并将对象空间传给__init__的self参数
# 3. 给对象封装相应的属性
# print(ret.__dict__)

# 对象的角度
# 操作对象中的静态变量
# 1. __dict__查询对象中的所有的内容
# 2. 万能的.  万能的点
# print(ret.name)  # 查
# ret.high = 177  # 增
# del ret.name  # 删
# ret.age = 73  # 改
# print(ret.__dict__)
# 对象操作对象中的静态变量： 只能查
# print(ret.mind)
# 对象调用类中的方法 （工作中 通过对象执行类中的方法，而不是通过类名）
# ret.shopp()
bigsum = Person('大秧歌', 19, "女人")
india_ning = Person('印度阿三', 28, '美女')
bigsum.work()
india_ning.work()

