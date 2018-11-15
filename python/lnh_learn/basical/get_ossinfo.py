#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

# -*- coding: utf-8 -*-
import oss2
from itertools import islice

# 阿里云主账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM账号进行API访问或日常运维，请登录 https://ram.console.aliyun.com 创建RAM账号。
auth = oss2.Auth('LTAIVk38GseWpVQY', 'ARBR2NHmzvbBBgH3HJtiaEeGzpBJjf')
# Endpoint以杭州为例，其它Region请按实际情况填写。
bucket = oss2.Bucket(auth, 'http://oss-cn-hangzhou.aliyuncs.com', 'my089-test')

# oss2.ObjectIteratorr用于遍历文件。
# for b in islice(oss2.ObjectIterator(bucket), 10):
#     print(b.key)

bucket.put_object_from_file('yqd/test.py', r'D:\python_learn\lnh_learn\basical\test.py')