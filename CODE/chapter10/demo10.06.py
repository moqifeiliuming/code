class Rectangle:
    def __init__(self):
        self.left = 0
        self.top = 0
    def setPosition(self,position):
        self.left,self.top = position
    def getPosition(self):
        return self.left,self.top

r = Rectangle()
r.left = 10
r.top = 20
print('left','=',r.left)
print('top','=',r.top)
r.setPosition([30,50])
print('position', '=', r.getPosition())

