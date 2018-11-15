#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# def func():
#     print("woshi momomo")
#     yield "hihihih"
#     print("woshi wwlih")
#     yield "jickw"
#     print("我是谁")
#     yield "我不会"
#
# g= func()  # 通过函数func() 来创建一个生成器
# for gg in g:
#     print(gg)

def func():
    print("砂锅粥")
    a = yield "11"
    print(a)
    print("狗不理")
    b = yield "22"
    print(b)
    print("大麻花")
    c = yield "33"
    print(c)


g = func()
print(g.__next__())
print(g.send(1))
print(g.send(2))
print(g.send(3))
# __next__()  可以让生成器向下执行一次
# send()  也可以让生成器向下执行一次,给上一个yield传一个值