#-*-coding:utf-8-*-
"""
__title__ = ''
__author__ = 'wux'
__mtime__ = '2018/12/9'
"""

# 属性的初识
# class Person:
#     def __init__(self, name, hight, weight):
#         self.name = name
#         self.__hight = hight
#         self.__weight = weight
#
#     @property
#     def bmi(self):
#         return '%s的BMI值为%s。' % (self.name, self.__weight / self.__hight ** 2)
#
#
# p1 = Person('wux', 1.77, 67)
# # print(p1.bmi())
# print(p1.bmi)
# # 属性：将一个方法伪装成属性，在代码的级别上没有本质的提升，但是让其看起来更合理
# p1.name = 'alex'
# print(p1.name)
# p1.bmi = 24
# print(p1.bmi)

# 属性的更改


class Person:
    def __init__(self, name, age):
        self.name = name
        if type(age) is int:
            self.__age = age
        else:
            print('您输入的类型有问题，请输入数字')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, a1):
        if type(a1) is int:
            self.__age = a1
        else:
            print('您输入的类型有问题，请输入数字')

    @age.deleter
    def age(self):
        print(666)


p1 = Person('wux', 18)
print(p1.age)
p1.age = 20
print(p1.age)
del p1.age
