#!/usr/bin/env python
# -*- encoding: utf-8 -*-


# 单例
# 如果一个类，从头到尾只能有一个实例，说明从头到尾只开辟了一块属于对象的空间，那么这个类就是一个单例类

# class A:pass
#
# a = A()
# a2 = A()
# a3 = A()
# print(a,a2,a3)

# 单例类

# class Single:
#     __ISINSTANCE = None
#     def __new__(cls, *args, **kwargs):
#         if not cls.__ISINSTANCE:
#             cls.__ISINSTANCE = object.__new__(cls)
#         return cls.__ISINSTANCE
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# s1 = Single('aaa', 18)
# print(s1.name)
# s2 = Single('bbb', 20)
# print(s1.name)
# print(s2.name)


class Student:
    def __str__(self):
        return "%s %s %s" % (self.name, self.school, self.cls)
    def __init__(self, name):
        self.name = name
        self.school = 'old boy'
        self.cls = 'py14'

he = Student('hezewei')
print(he)
huang = Student('huangdongyang')
print(huang)

# print一个对象相当于调用一个对象的__str__方法
# str(obj) 相当于执行obj.__str__方法
# '%s' % obj 相当于执行obj.__str__方法
print(str(he))  # 内置的数据类型，内置的类，相当于执行__str__
print('学生 %s' % he)


# __call__ 相当于对象()
# __len__ 相当于len(obj)
# __new__ 特别重要，开辟内存空间  类的构造方法
# __str__ str(obj)  '%s' % obj
# 所有的双下方法没有需要你在外部直接调用的
# 总有其他的内置函数  特殊语法 来自动触发这些双下方法