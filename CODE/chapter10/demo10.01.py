class Person:
    def __init__(self,name = "Bill"):
        print("构造方法已经被调用")
        self.name = name
    def getName(self):
        return self.name
    def setName(self,name):
        self.name= name

person = Person()
print(person.getName())
person1 = Person(name = "Mike")
print(person1.getName())
person1.setName(name = "John")
print(person1.getName())