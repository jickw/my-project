#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# lst = [i for i in range(1, 8)]
#
# def func(i):
#     return i*i
#
# print(list(map(func, lst)))  # 把可迭代对象中的每一个元素传递给前面的函数进行处理，处理结果会返回

lst1 = [1,2,3,4,5]
lst2 = [2,4,6,8,10]

print(list(map(lambda x, y: x+y, lst1, lst2)))   # 如果函数中有多个参数，后面对应的列表要一一对应
