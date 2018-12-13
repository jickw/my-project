#-*-coding:utf-8-*-
"""
__title__ = ''
__author__ = 'wux'
__mtime__ = '2018/12/13'
"""

'''
什么是反射
用字符串数据类型的变量名来访问这个变量的值

反射的方法： getattr   hasattr   setattr   delattr

类
class Student:
    def __init__(self):
        pass

    def check_course(self):
        print('check course')

    def choose_course(self):
        print('choice course')

    def choosed_course(self):
        print('查看已选择的课程')


stu = Student()

num = input('>>>')
if num == 'check_couse':
    stu.check_course()
elif num == 'choose_course':
    stu.choose_course()
elif num == 'choosed_course':
    stu.choosed_course()
对象
模块
反射自己模块中的内容


eval 这个明确的写在你的代码里才可以用
'''


# class Student:
#     ROLE = 'STUDENT'
#
#     @classmethod
#     def check_course(cls):
#         print('查看课程')
#
#     @staticmethod
#     def login():
#         print('登录')
#
#
# print(getattr(Student, 'ROLE'))
# 取出第一个参数的命名空间中的变量名为第二个参数的变量的值
# getattr(Student, 'check_course')()
# getattr(Student, 'login')()

# num = input('>>>')
# if hasattr(Student, num):
#     getattr(Student, num)()

# def wahaha():
#     print('wahaha')
#
# def qqxing():
#     print('qqxing')
#
#
# import sys
# import 相当于导入了一个模块
# import sys 是一个模块，这个模块里的所有方法都是和python解释器相关的
# sys.modules 这个方法表示所有在当前这个python程序中导入的模块
# '__main__':

# print(sys.modules['__main__'])
# getattr(sys.modules['__main__'], 'wahaha')()

# 反射
# hasattr    getattr
# 类名.名字
# getattr(类名,名字)
# 对象名.名字
# getattr(对象名,名字)
# 模块名.名字
# getattr(模块名,名字)
# 自己文件.名字
# import sys
# getattr(sys.modules['__main__'], '名字')
class Manager:
    OPERATE_DICT = [
        ('创造学生账号', 'create_student'),
        ('创建课程', 'create_course'),
        ('查看学生信息', 'check_student_info')
    ]
    def __init__(self, name):
        self.name = name

    def create_student(self):
        print('创建学生账号')

    def create_course(self):
        print('创建课程')

    def check_student_info(self):
        print('查看学生信息')


class Student:
    OPERATE_DICT = [
        ('check_course', 'check_course'),
        ('choose_course', 'choose_course'),
        ('查看已选择的课程', 'choosed_course')
    ]
    def __init__(self, name):
        self.name = name

    def check_course(self):
        print('check_course')

    def choose_course(self):
        print('choice course')

    def choosed_course(self):
        print('查看已选择的课程')




def login():
    username = input('user: ')
    password = input('pwd: ')
    with open('userinfo') as f:
        for line in f:
            user,pwd,ident = line.strip().split('|')
            if user == username and pwd == password:
                print('登录成功')
                return username, ident

import sys
def main():
    usr, id = login()
    file = sys.modules['__main__']
    cls = getattr(file, id)
    obj = cls(usr)
    operate_dict = cls.OPERATE_DICT
    # print(operate_dict)
    while True:
        for num, i in enumerate(operate_dict, 1):
            print(num, i[0])
        choice = int(input('num >>>'))
        choice_item = operate_dict[choice-1]
        getattr(obj, choice_item[1])()


# if __name__ == '__main__':
#     main()

class A:
    def __init__(self, name):
        self.name = name


a = A('alex')
# a.name = 'alex_wux'
setattr(a, 'name', 'alex_wux')
print(a.name)
