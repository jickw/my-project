#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# lst = [1, 2, 3]
# str, list, tuple, set, file, dict
# 以上数据类型中都有一个函数__iter__(), 所有包含了__iter__()的数据类型都是可迭代的数据类型Iterable
# dir()来查看一个对象，数据类型中包含了哪些东西
# print(dir(lst))

# lst = ["皇阿玛", "皇额娘", "容嬷嬷", "紫薇"]
# 获取迭代器
# it = lst.__iter__()
# 迭代器往外拿元素，__next__()
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())  # 迭代到最后一个元素之后，再进行迭代就报错了

# lst = ["皇阿玛", "皇额娘", "容嬷嬷", "紫薇"]
#
# it = lst.__iter__()
# while True:
#     try:
#         name = it.__next__()
#         print(name)
#     except StopIteration:  # 拿完了
#         break

lst = [1, 2, 3]
from collections import Iterator,Iterable

print(isinstance(lst, Iterable))
print(isinstance(lst, Iterator))
