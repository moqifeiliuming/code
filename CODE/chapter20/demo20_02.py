
'''
    测试square函数
    >>> square(2)
    4
    >>> square(6)
    36
    
    测试add函数
    >>> add(2,2)
    4
    >>> add(4,5)
    9
'''
def square(x):
    return x * x

def add(x,y):
    return x + y
 
if __name__ == '__main__':
    import doctest,demo20_02
    doctest.testmod(demo20_02)
    