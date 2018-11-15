#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
此代码用于生成长度为20 的随机密码
"""

import string,random

# symbol = r'#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
symbol_ali = r'!@#$%^&*()_+-='
symbol_alidrds = r'@#$%^&+='
strings = string.ascii_letters
numbers = string.digits
# with_symbol = strings + numbers + symbol
with_alisymbol = strings + numbers + symbol_ali
without_symbol = strings + numbers + '_'
with_alidrdssymbol = strings + numbers + symbol_alidrds


# print('_'*50)
# print("生成随机密码包含大小写字母，数字，字符")
# print('_'*50)
# for secret in [''.join([random.choice(with_symbol) for _ in range(20)]) for _ in range(50)]:
#     print(secret)

print('_'*50)
print("生成随机密码字符大小写字母，数字，_")
print('_'*50)
for secret1 in [''.join([random.choice(without_symbol) for _ in range(20)]) for _ in range(50)]:
	print(secret1)

print('_'*50)
print("生成随机密码字符大小写字母，数字，阿里规定RDS字符")
print('_'*50)
for secret1 in [''.join([random.choice(with_alisymbol) for _ in range(20)]) for _ in range(50)]:
	print(secret1)

print('_'*50)
print("生成随机密码字符大小写字母，数字，阿里规定DRDS字符")
print('_'*50)
for secret1 in [''.join([random.choice(with_alidrdssymbol) for _ in range(20)]) for _ in range(50)]:
	print(secret1)
