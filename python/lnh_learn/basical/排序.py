#!/usr/bin/env python
# -*- encoding: utf-8 -*-

lst = [22, 33, 11, 4, 41, 32]

for i in range(7):
    i = 0
    while i < len(lst)-1:
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
        i = i+1
print(lst)