import sys

# sys.path.append('E:\my-project\python\lnh_learn\\201901\\0103\模块导入练习\core')
# print(sys.path)
#
# import main
# main.entry_point()

print(__file__)
ret = __file__.split('/')
basepath = '/'.join(ret[:-2])
print(basepath)
sys.path.append(basepath)
from core import main
main.entry_point()

