#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# lst1 = ['超人', '七龙珠', '葫芦娃', '山中小猎人', ['金城武', '王力宏', '渣渣辉']]

# lst2 = lst1.copy()   # 浅拷贝

# lst1[4].append('大秧歌')

# print(lst1, lst2)


import copy

lst1 = ['超人', '七龙珠', '葫芦娃', '山中小猎人', ['金城武', '王力宏', '渣渣辉']]

lst2 = copy.deepcopy(lst1)    # 把lst1扔进去进行深度拷贝，包括内部的所有内容进行拷贝

lst1[4].append('刘德华')

print(lst1, lst2)