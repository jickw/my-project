#-*-coding:utf-8-*-
"""
__title__ = ''
__author__ = 'wux'
__mtime__ = '2018/12/13'
"""

# isinstance()   判断对象所属类型，包括所属对象，继承关系



# class A:
#     pass
#
#
# class B(A):
#     pass
#
#
# b = B()
# print(isinstance(b, A))

# == 值相等     值运算
# is 内存地址相等  身份运算
# is要求更苛刻   不仅要求值相等，还要求内存地址相同


# issubclass()  判断类与类之间的关系


class A:
    pass


class B(A):
    pass


print(issubclass(B, A))

print(issubclass(A, B))
