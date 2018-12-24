#!/usr/bin/env python
# -*- encoding: utf-8 -*-

start = 2000
count = 0
for i in range(10):
    count += start * 12
    start += 100
    print('%s...%s'%(start, count))