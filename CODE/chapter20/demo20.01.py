import math
def circleArea(r):
    return math.pi * r * r
r = 20
if r <= 0:
    print('测试失败，圆半径必须大于0')
area = circleArea(r)
if area > 1000:
    print('测试失败，圆的面积不能大于1000')
else:
    print('测试成功')
 