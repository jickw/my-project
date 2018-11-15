#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import sys

sys.setrecursionlimit(10000)  # 可以调整递归深度，但是不一定能跑到这里

def func(count):
    print("who am I ?", count)
    func(count+1)

func(1)

# 遍历树型结构
