class MyParentClass:
    def method(self):
        return 50
class ParentClass(MyParentClass):
    def method1(self):
        print("method1")
class MyClass:
    def method(self):
        return 40
class ChildClass(ParentClass):
    def method2(self):
        print("method2")
print(issubclass(ChildClass, ParentClass))
print(issubclass(ChildClass, MyClass))
print(issubclass(ChildClass, MyParentClass))

print(ChildClass.__bases__)
print(ParentClass.__bases__)

child = ChildClass()
print(isinstance(child, ChildClass))
print(isinstance(child, ParentClass))
print(isinstance(child, MyParentClass))

print(isinstance(child, MyClass))
        
