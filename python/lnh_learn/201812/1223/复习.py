#-*-coding:utf-8-*-
"""
__title__ = ''
__author__ = 'wux'
__mtime__ = '2018/12/23'
"""

# 抽象类和接口类
# 不能被实例化
# 规范子类当中必须实现某个方法
# 有原生的实现抽象类的方法，但是没有原生实现接口类的方法

# java 只支持类的单继承
# 接口interface支持多继承的规范，接口中的所有方法 只能写pass

# 多态
# 鸭子类型  规范全凭自觉

# 封装   私有的
# 广义的封装： 把方法和属性都封装在一个类里，定义一个规范来描述一类事务
# 狭义的封装： 私有化，只能在类的内部访问
# __静态变量： 私有方法，私有的对象属性，私有的类方法，私有的静态方法
# 在内存中存储 __类名__名字

# 为什么在类的内部都可以使用双下划线访问；在类的内部使用，你就知道你在哪个类中
# 在子类中可以访问父类的私有变量么？不行
# 私有： 不能在类的外部使用也不能被继承

# property  装饰器函数，内置函数，帮助你将类中的方法伪装成属性，特性
# 调用方法的时候不需要主动加括号
# 让程序的逻辑性更合理
# @方法名.setter  装饰器：修改被property装饰的属性的时候会调用这个装饰器装饰的方法，除了self之外还有一个参数，被修改的值
# @方法名.deletter  装饰器： 当要删除被property装饰的属性的时候会调用这个装饰器装饰的方法

# class Circle:
#     def __init__(self, r):
#         self.r = r
#         # self.area = self.r**2*3.14
#
#     @property
#     def area(self):
#         return self.r**2*3.14
#
#
# c = Circle(5)
# print(c.area)
# c.r = 10
# print(c.area)
#


# 反射
# 从某个指定的命名空间中，用字符串数据类型的变量名来获取变量的值

# 类名反射
# 对象反射
# 模块
# 自己的模块



