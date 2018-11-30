#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# 面向对象三大特性： 继承，多态， 封装

# 继承

class Animal:
    breath = "呼吸"

    def __init__(self, name , sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def eat(self):
        print('吃东西')

    def drink(self):
        print('喝东西')

class Cat(Animal):
    pass

class Dog(Animal):
    pass

class Chook(Animal):  # 括号里面的  父类，基类， 超类  括号外面的 子类， 派生类
    pass

