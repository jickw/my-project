class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if self.name == other.name and self.age == other.age:
            return True


a = A('wux',19)
aa = A('wux', 19)
aa2 = A('wux', 19)
print(a, aa)
print(a == aa == aa2)  # == 这个语法是和__eq__相关

