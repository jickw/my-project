import sys
print(__name__)
print(sys.modules['__main__'])
print(sys.modules[__name__])

def func():
    print('aaa')

getattr(sys.modules[__name__], 'func')()