#-*-coding:utf-8-*-
"""
__title__ = ''
__author__ = 'wux'
__mtime__ = '2018/11/3'
"""

# f = open("歌姬", mode='r', encoding='utf-8')
# s = f.read()
# f.close()   # 关闭文件句柄
# print(s)
#

# f = open('模特', mode='w', encoding='utf-8')
# f.write('刘雯')
# f.close()

# f = open('模特', mode='a', encoding='utf-8')
# f.write('奚梦瑶')
# f.flush()
# f.close()

# f = open('模特', mode='rb')
# bs = f.read()
# print(bs.decode('utf-8'))
# f.close()
#
# f = open('模特', mode='wb')
# bs = f.write('你好'.encode('utf-8'))
# f.close()

# w,r === wb, rb b:处理的是非文本


f = open("吃的", mode='r', encoding='utf-8')
for line in f:   # 每次读取一行， 赋值给前面的line变量
    print(line)
f.close()   # 关闭文件句柄
