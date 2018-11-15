#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# lst = [5, 7, 6, 12, 44, 7, 23, 3]
# # lst.sort()
# # print(lst)
#
# ll = sorted(lst, reverse=True)  # 内置函数，返回一个新列表 新列表是被排序的
# print(ll)

# 给列表排序，根据字符串的长度进行排序
# lst = ["小沈阳", "赵a", "赵能aaaaaaaa", "谢大脚是谁aa", "欧阳大大aaa"]
#
# a = lambda x:x.count('a')  # 返回数字
#
# ll = sorted(lst, key=a)  # 内容，把可迭代对象中的每一个元素传递给func
# print(ll)


lst = [
    {'id':1, 'name':'alex','age':18},
    {'id': 2, 'name': 'taibai', 'age': 58},
    {'id': 3, 'name': 'wusir', 'age': 38},
    {'id': 4, 'name': 'ritian', 'age': 48},
    {'id': 5, 'name': 'nvshen', 'age': 18}
]

# a = lambda x:x['age']
#
# ll = sorted(lst, key=a)
# print(ll)

print(list(filter(lambda dic:dic['age']>40, lst)))
