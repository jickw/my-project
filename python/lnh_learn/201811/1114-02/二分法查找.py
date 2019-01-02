#-*-coding:utf-8-*-
"""
__title__ = ''
__author__ = 'wux'
__mtime__ = '2018/11/14'
"""

# lst = [i for i in range(0, 100, 2)]
# n = 66
# left = 0
# right = len(lst) - 1
# count = 1
# while left <= right:
#     middle = (left + right) // 2
#     if n > lst[middle]:
#         left = middle + 1
#     elif n < lst[middle]:
#         right = middle - 1
#     else:
#         print(count)
#         print("存在")
#         print(middle)
#         break
#     count = count + 1
# else:
#     print("不存在")
#
lst = [11, 22, 33, 44, 55, 66, 77, 88, 99, 123, 234, 345, 456, 567, 678, 789, 890]
#
#
# def binary_search(left, right, n):
#     middle = (left + right) // 2
#     if n > lst[middle]:
#         left = middle + 1
#     elif n < lst[middle]:
#         right = middle - 1
#     else:
#         return middle
#     return binary_search(left, right, n)
#
#
# print(binary_search(0, len(lst)-1, 66))


def binary_search(lst, n):
    left = 0
    right = len(lst) - 1
    if left > right:
        print("不存在")
        return -1
    middle = left+right//2
    if n > lst[middle]:
        lst = lst[middle+1:]
    elif n < lst[middle]:
        lst = lst[:middle-1]
    else:
        print("找到了")
        return
    binary_search(lst, n)


binary_search(lst, 65)
