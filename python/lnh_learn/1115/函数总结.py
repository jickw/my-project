#!/usr/bin/env python
# -*- encoding: utf-8 -*-

def func(*args):
    print(*args)
    # print(**kwargs)


# * ：当定义一个函数的时候： *代表聚合
# 当执行一个函数的时候： * 代表打散
# func(1, 2, 3, name='alex', age=10000)
l1 = [1, 2, 3]
l2 = [4, 5, 6]
func(l1, l2)
