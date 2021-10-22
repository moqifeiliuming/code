class MyClass:
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
        self.__outName()
        
    def __outName(self):
        print("Name = {}".format(self.name))        


myClass = MyClass()
import inspect
methods = inspect.getmembers(myClass, predicate=inspect.ismethod)
print(methods)
for method in methods:
    print(method[0])
print("------------")
myClass.setName("Bill")
print(myClass.getName())
myClass._MyClass__outName()
print(myClass.__outName())

