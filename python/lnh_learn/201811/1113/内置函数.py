#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# a = 10
#
# print(callable(a))
#
# def func():
#     print("aaa")
#
# print(callable(func))

# s = input("请输入a+b： ")
#
# print(eval(s))   #  可以动态的执行代码，代码必须有返回值

# s = "for i in range(10): print(i)"
#
# print(eval(s))

# s = "for i in range(10): print(i)"
# a = exec(s)  # exec 执行代码不返回任何内容
# print(a)

# exec("""
# def func():
#     print("i am jack")
#
# """)
#
# func()

# code1 = "for i in range(10): print(i)"
# com = compile(code1, "", mode="exec")  # compile并不会执行你的代码，只是编译
# exec(com) # 执行编译之后的结果
#
# code2 = "5+2+7"
# com2 = compile(code2, "", mode="eval")
# print(com2)
# print(eval(com2))

# code3 = "name = input('请输入大秧歌的名字： ')"
# com3 = compile(code3, "", mode="single")
# exec(com3)
# print(name)

# print(abs(-2))  # 求绝对值
# print(abs(2))

# print(divmod(20, 3))  # 求商和余数

# print(round(4.5))

# print(pow(10, 2, 3))  # 如果给了第三个参数，表示最后取余

# print(sum([1, 3, 4, 65, 6, 3]))

# lst = "nihaoya"
# it = reversed(lst)
# print(list(it))

# lst = [1,2,3,4,5,6,7]
# print(lst[1:3:1])
# s = slice(1,3,1)
# print(lst[s])
#
# name = "你好， \n我是%s吴宣"
#
# print(name)
# print(repr(name))  # 原样输出

# print(ord('a'))  # 返回字母a在编码集中的码位
# print(ord("中"))

# print(chr(97))  # 已知码位，计算字符
#
# print(chr(20018))

# for i in range(65536):
#     print(chr(i), end=" ")

# print(ascii('过'))
#
# s = '李嘉诚的爸爸'
# a = s.encode("UTF-8")
# print(a)
# print(a.decode("GBK"))


# bs = bytes("大家我怕 打飞机的", encoding="utf-8")
# print(bs)
# print(bs.decode("utf-8"))

# ret = bytearray('alex', encoding="utf-8")
# print(ret)
# ret[0] = 65
# print(str(ret))

# s = memoryview("你好".encode("UTF-8"))
# print(s)

# s = "我叫吴宣"
# print(format(s, "^20"))
# print(format(s, "<20"))
# print(format(s, ">20"))

# print(format(3, 'b'))  # 二进制
# print(format(97, 'c'))  # 转换成unicode字符
# print(format(11, 'd'))  # 十进制%d
# print(format(11, 'o'))  # 八进制 8
# print(format(11, 'x'))  # 十六进制(小写字母)
# print(format(11, 'X'))  # 十六进制(大写字母)
# print(format(11, 'n'))  # 和d一样
# print(format(11))  # 和d一样

# print(format(123456789, 'e'))  # 科学计数法， 默认保留6位小数
# print(format(123456789, '0.2e'))  # 科学计数法， 默认保留2位小数（小写）
# print(format(123456789, '0.2E'))  # 科学计数法， 默认保留2位小数（大写）
# print(format(1.23456789, 'f'))  # 小数点计数法，保留6位小数
# print(format(1.23456789, '0.2f'))  # 小数点计数法，保留2位小数
# print(format(1.23456789, '0.10f'))  # 小数点计数法，保留10位小数
# print(format(1.23456789e+10000, 'F'))  # 小数点计数法，很大的时候输出INF

# lst = ["蛋1", "蛋2", "蛋3", "蛋4", ]
# # for i in range(len(lst)):
# #     print(i)
# #     print(lst[i])
#
# for index, el in enumerate(lst, 1):  # 把索引和元素一起获取,索引默认从0开始，可以更改
#     print(index)
#     print(el)

# print(all([1, "aaa", 0, "True"]))
# print(any([1, "aaa", 0, "True"]))

l1 = [1, 2, 3]
l2 = ['a', 'b', 'c', 5]
l3 = ('*', '**', '***', '**', '*')

for i in zip(l1, l2, l3):
    print(i)
