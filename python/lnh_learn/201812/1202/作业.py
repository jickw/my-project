#-*-coding:utf-8-*-
"""
__title__ = ''
__author__ = 'wux'
__mtime__ = '2018/12/2'
"""

# class Animal:
#     def __init__(self, name, sex, age):
#         self.name = name
#         self.sex = sex
#         self.age = age
#
#     def eat(self):
#         print('%s在吃东西' % self.name)
#
# class Person(Animal):
#     def __init__(self, name, sex, age, skin):
#         super().__init__(name, sex, age)
#         self.skin = skin
#
#     def eat(self):
#         print('人类在吃饭')
#
#
# class Dog(Animal):
#     def __init__(self, coat_color):
#         self.coat_color = coat_color
#
#     def eat(self):
#         print('狗狗在吃饭')
#
#
# p1 = Person('李富贵', '男', 18, '黄皮肤')
# print(p1.__dict__)
# p1.eat()
#
# class Parent:
#     def func(self):
#         print('in Parent func')
#
#     def __init__(self):
#         self.func()
#
# class Son(Parent):
#     def func(self):
#         print('in Son func')
#
# son1 = Son()


class A:
    name = []


p1 = A()
p2 = A()

p1.name.append(1)

print(p1.name)
print(p2.name)
print(A.name)

