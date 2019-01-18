#-*-coding:utf-8-*-
"""
__title__ = ''
__author__ = 'wux'
__mtime__ = '2019/1/18'
"""
import json
# 如果是数据  json
dic = {1:2,3:4}
str_dic = json.dumps(dic)
print(str_dic)
new_dic = json.loads(str_dic)
print(new_dic)