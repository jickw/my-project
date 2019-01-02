#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# python中没有接口概念
#
# 接口类，抽象类：定义，制定一个规范

# 第一版
# class Alipay:
#     def __init__(self, money):
#         self.money = money
#
#     def pay(self):
#         print('使用支付宝支付了%s' % self.money)
#
#
# class Jdpay:
#     def __init__(self, money):
#         self.money = money
#
#     def pay(self):
#         print('使用京东支付了%s' % self.money)
#
#
# a1 = Alipay(200)
# a1.pay()
#
# j1 = Jdpay(100)
# j1.pay()

# 第二版  改进  让你支付的方式一样
# class Alipay:
#     def __init__(self, money):
#         self.money = money
#
#     def pay(self):
#         print('使用支付宝支付了%s' % self.money)
#
#
# class Jdpay:
#     def __init__(self, money):
#         self.money = money
#
#     def pay(self):
#         print('使用京东支付了%s' % self.money)
#
#
# def pay(obj):
#     obj.pay()
#
#
# a1 = Alipay(200)
# j1 = Jdpay(100)
# pay(a1)
# pay(j1)


# 第三版 增加一个微信支付
#
# class Alipay:
#     def __init__(self, money):
#         self.money = money
#
#     def pay(self):
#         print('使用支付宝支付了%s' % self.money)
#
#
# class Jdpay:
#     def __init__(self, money):
#         self.money = money
#
#     def pay(self):
#         print('使用京东支付了%s' % self.money)
#
#
# class Wechatpay:
#     def __init__(self, money):
#         self.money = money
#
#     def weixinpay(self):
#         print('使用微信支付了%s' % self.money)
#
# def pay(obj):
#     obj.pay()
#
#
# a1 = Alipay(200)
# j1 = Jdpay(100)
# pay(a1)
# pay(j1)
#
# w1 = Wechatpay(300)
# w1.weixinpay()

# 第四版  制定规则  抽象类，接口类
from abc import ABCMeta, abstractmethod

class Payment(metaclass=ABCMeta):   #  抽象类（接口类）  强制指定一个规范，凡是集成此类的类中必须有一个pay方法，若没有，实例化对象的时候会报错
    @abstractmethod
    def pay(self):  # 制定了一个规范
        pass

class Alipay(Payment):
    def __init__(self, money):
        self.money = money

    def pay(self):
        print('使用支付宝支付了%s' % self.money)


class Jdpay(Payment):
    def __init__(self, money):
        self.money = money

    def pay(self):
        print('使用京东支付了%s' % self.money)


class Wechatpay(Payment):
    def __init__(self, money):
        self.money = money

    def pay(self):
        print('使用微信支付了%s' % self.money)

def pay(obj):
    obj.pay()


a1 = Alipay(200)
j1 = Jdpay(100)
pay(a1)
pay(j1)
#
w1 = Wechatpay(300)
w1.pay()


