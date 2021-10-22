class ParentClass:
    name = 30
    def method1(self):
        print("method1")
class ChildClass(ParentClass):
    def method2(self):
        print("method2")
        print(self.name)

child = ChildClass()
child.method1()
child.method2()
        
