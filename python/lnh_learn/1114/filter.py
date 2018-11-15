#!/usr/bin/env python
# -*- encoding: utf-8 -*-

def func(i):
    return i%2 == 1


lst = [i for i in range(1,10)]

# ll = filter(func, lst)
ll = filter(lambda x:x%2==1, lst)
# 第一个参数，函数，将第二个参数中的每一个元素传递给函数，函数如果返回True，留下该元素
# print("__iter__" in dir(ll))
# print("__next__" in dir(ll))

print(list(ll))