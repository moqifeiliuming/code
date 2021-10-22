class Person:
    def setName(self, name):             
        self.name = name
    def getName(self):        
        return self.name
    def greet(self):
        print("Hello, I'm {name}.".format(name = self.name))

person1 = Person()
person2 = Person()

person1.setName("Bill Gates")
person2.name = "Bill Clinton"

print(person1.getName())
person1.greet()
print(person2.name)
Person.greet(person2)
