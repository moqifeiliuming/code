class MyClass:
    print("MyClass")
    count = 0
    def counter(self):
        self.count += 1

my = MyClass()
my.counter()
print(my.count)
my.counter()
print(my.count)
my.count = "abc"
print(my.count)
my.name = "Hello"
print(my.name)

