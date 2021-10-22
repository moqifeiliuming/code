import math
import profile
def circleArea(r):
    return math.pi * r * r
def sub(x,y):
    return x - y
def test():
    for i in range(10,20):
        print(circleArea(i))
        if i % 2 == 0:
            print(sub(circleArea(i * i) ,10))
profile.run('test()','test.profile')