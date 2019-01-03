# item系列  和对象使用[]访问值有关

# 有一些特殊方法，要求对象必须实现__getitem__和__setter__方法才能使用
# class B:
#     def __init__(self, lst):
#         self.lst = lst
#
#     def __getitem__(self, item):
#         # return getattr(self, item)
#         return self.lst[item]
#
#     def __setitem__(self, key, value):
#         setattr(self, key, value)
#
#     def __delitem__(self, key):
#         delattr(self, key)
# b['k1'] = 'v1'
# print(b['k1'])
# del b['k1']
# print(b['k1'])


class B:
    def __init__(self, lst):
        self.lst = lst

    def __getitem__(self, item):
        # return getattr(self, item)
        return self.lst[item]

    def __setitem__(self, key, value):
        self.lst[key] = value

    def __delitem__(self, key):
        self.lst.pop(key)


b = B(['111', '222', 'ccc', 'ddd'])
# print(b.lst[0])
print(b[0])
b[3] = 'wux'
print(b.lst)
del b[2]
print(b.lst)

