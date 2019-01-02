#!/usr/bin/env python
# -*- encoding: utf-8 -*-

class A:
    def __init__(self, name, age, weight):
        self.name = name
        self.__age = age
        self.__weight = weight

    def func(self):
        print(self.__age)

a1 = A('alx', 18, 120)
# print(a1.__dict__)
# print(a1.name)
# print(a1.__age)

a1.func()