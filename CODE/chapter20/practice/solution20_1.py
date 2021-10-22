'''
    测试factorial函数
    >>> factorial(1)
    1
    >>> factorial(2)
    2
    >>> factorial(4)
    24
    >>> factorial(6)
    720
'''
def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return factorial(n - 1) * n


 
if __name__ == '__main__':
    import doctest,solution20_1
    doctest.testmod(solution20_1)
    