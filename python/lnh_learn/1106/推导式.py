#!/usr/bin/env python
# -*- encoding: utf-8 -*-

def add(a, b):
    return a + b

def test():
    for i in range(4):
        yield i

g = test()

for n in [2, 10]:
    g = (add(n, i) for i in g)

print(list(g))