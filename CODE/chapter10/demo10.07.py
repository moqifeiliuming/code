class Rectangle:
    def __init__(self):
        self.left = 0
        self.top = 0
    # setPosition方法可以是其他的名字
    def setPosition(self,position):
        print('setPosition方法被调用')
        self.left,self.top = position
    # getPosition方法可以是其他的名字        
    def getPosition(self):
        print('getPosition方法被调用')
        return self.left,self.top
    def deletePosition(self):
        print('position属性已经被删除')
        self.left = 0
        self.top = 0
 
    position = property(getPosition, setPosition,deletePosition)

r = Rectangle()
r.left = 10
r.top = 20
print('left','=',r.left)
print('top','=',r.top)
print('position', '=', r.position)
r.position = 100,200
print('position', '=', r.position)
del r.position
print(r.position)
r.position = 30,40
print('r.position','=',r.position)

        