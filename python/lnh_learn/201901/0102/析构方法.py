
# 构造方法  申请一个空间
# 析构方法  释放一个空间
# 某对象借用了操作系统的资源，还要通过析构方法归还回去： 文件资源， 网络资源

# 不管是主动还是被动，这个f对象总会被清理掉，被清理掉就触发__del__方法，触发这个方法就会归还操作系统的文件资源


class File:
    # 处理文件的
    def __init__(self, file_path):
        self.f = open(file_path)

    def read(self):
        self.f.read(1024)

    def __del__(self):  # 是去归还/释放一些在创建对象的时候借用的一些资源
        # del 对象的时候
        # python解释器的垃圾回收机制  回收这个对象所占得的内存的时候    python自动触发的
        self.f.close()


f = File('file.txt')
f.read()
