class MyClass:
    name = "Bill"
    def __init__(self):
        print("MyClass的构造方法被调用")
        self.value = 20
    @staticmethod
    def run():
        print('*', MyClass.name, '*')
        print("MyClass的静态方法run被调用")
    @classmethod
    # 这里self是元数据
    def do(self):
        print(self)
        print('[', self.name, ']')
        print('调用静态方法run')
        self.run()
        # 如果是类方法，就无法访问self中的成员变量了
        #print(self.value)
        print("成员方法do被调用")
    def do1(self):
        print(self.value)
        print('<',self.name, '>')
        print(self)
        
MyClass.run()
c = MyClass()
c.do()
print('MyClass2.name','=',MyClass.name)
MyClass.do()
c.do1()



