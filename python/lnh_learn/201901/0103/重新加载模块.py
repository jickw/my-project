import aaa
import time
import importlib
aaa.login()
time.sleep(20)
importlib.reload(aaa)  # 表示重新加载模块
# 在import之后，再修改这个被导入的模块
# 程序感知不到

aaa.login()
