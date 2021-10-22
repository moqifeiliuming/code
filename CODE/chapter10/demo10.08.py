class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
        self.left = 0
        self.top = 0
    def __setattr__(self,name,value):        
        print("{}被设置，新值为{}".format(name,value))
        if name == 'size':
            self.width, self.height = value
        elif name == 'position':
            self.left, self.top = value
        else:
            self.__dict__[name] = value  # 必须加上

    def __getattr__(self,name):
        print("{}被获取".format(name))
        if name == 'size':
            return self.width,self.height
        elif name == 'position':
            return self.left, self.top 

    def __delattr__(self,name):
        if name == 'size':
            self.width,self.height = 0, 0
        elif name == 'position':
            self.left, self.top = 0,0
r = Rectangle()
r.size = 300,500
r.position = 100,400
print('size', '=', r.size)
print('position', '=', r.position)
del r.size, r.position
print(r.size)
print(r.position)


class MyClass:
     def __setattr__(self,name,value):        
        if name == 'value':
            if value > 0:
                self.__dict__[name] = value
            else:
                print('{}属性的值必须大于0'.format(name))
        else:
           self.__dict__[name] = value
c = MyClass()
c.value = 20
print('c.value','=',c.value)
c.value = -43
print('c.value','=',c.value)
