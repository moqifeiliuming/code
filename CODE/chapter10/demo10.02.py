
class Bird:
    def __init__(self):
        self.hungry= True
    def eat(self):
        if self.hungry:
            print("已经吃了虫子！")
            self.hungry = False
        else:
            print("已经吃过饭了，不饿了！")
b = Bird()
b.eat()
b.eat()

class SongBird(Bird):
    def __init__(self):
        self.sound = '向天再借五百年'
    def sing(self):
        print(self.sound)
    def eat(self,thing):
        print(thing)
        
sb = SongBird()
sb.sing()
sb.eat()