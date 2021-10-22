#析构方法
class animal:
    def __init__(self,name):
        self.name=name;
        print('这是构造初始化方法')
        pass

    def __del__(self):  #操作对象的释放，一旦释放后，对象便不能使用
        print('当在某个作用域下面，没有被使用【引用】的情况下，解析器会自动地调用此函数来释放内存空间')
        print('这是析构方法')
        print('%s 这个对象被彻底释放掉了'%self.name)
    pass

# cat=animal('小花猫')
# del cat  手动删除对象，会指定__del__函数

#析构方法总结：1、当整个程序脚本执行完毕后会自动调用__del__方法
#2、当对象被手动销毁时也会自动调用__del__方法
#3、析构函数一般用于资源回收，利用__del__方法销毁对象回收内存等资源

#封装：指的是把内容封装到某个地方，便于后面的使用；对于封装来说，其实就是使用初始化构造方法将内容封装到对象中，然后通过对象直接或者self来获取被封装的内容
#继承：子可以继承父类的内容【属性和行为】，可以极大的提高效率，减少代码的重复编写

#单继承
class Animal:
    def eat(self):
        print('吃饭了')
        pass

    def drink(self):
        print('喝东西了')
        pass

class Dog(Animal):
    def wwj(self):
        print('小狗汪汪叫')
        pass

class Cat(Animal):
    def mmj(self):
        print('小猫喵喵叫')
        pass

dog=Dog()
dog.eat()
dog.drink()
dog.wwj()
cat=Cat()
cat.eat()
cat.drink()
cat.mmj()

#多继承
class shenXian:
    def fly(self):
        print("神仙都会飞")
    pass

class Monkey:
    def chitao(self):
        print("喜欢吃桃")
    pass

class Sunwukong(shenXian,Monkey):
    pass

swk=Sunwukong()
swk.fly()
swk.chitao()
#结果：神仙都会飞   喜欢吃桃

class D:
    def eat(self):
        print('D eat')
        pass
    pass
class C(D):
    def eat(self):
        print('C eat')
        pass
    pass
class B(D):
    pass
class A(B,C):
    pass
a=A()
a.eat()
#结果：C eat   查找方法的顺序：首先到A中进行查找，如果A中没有，则将从B类中查找，若B中没有，就去C类中去查找，如果C类中没有，则去D类中查找，假使D中仍没有，则报错
print(A.__mro__)  #顺序：A--B--C--D--Object
#<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class 'object'>

class GrandFather:
    def eat(self):
        print('吃的方法')
        pass
    pass
class Father(GrandFather):
    def eat(self):    #相当于方法重写，直接方法覆盖了
        print('经常吃海鲜')
    pass
class Son(Father):
    pass
son=Son()
print(Son.__mro__)  #(<class '__main__.Son'>, <class '__main__.Father'>, <class '__main__.GrandFather'>, <class 'object'>)
son.eat()  #此方法是从GrandFather中继承过来的，只要找到一个就停止查找了
#重写：子类中，有一个和父类相同名字的方法，在子类中的方法会覆盖掉父类的方法

class Dog:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    
    def bark(self):
        print('汪汪叫')
        pass
    pass

class keji(Dog):
    def __init__(self,name,color):
        Dog.__init__(self,name,color) #手动调用父类的方法
        #super().__init__(name,color) #自动找到父类，进而调用方法，如继承了多个父类，会按照顺序逐个去寻找调用
        #拓展其他属性
        self.height=90
        self.weight=20
    pass

    def __str__(self):
        return '{}的颜色是{},它的身高是{}cm 体重是{}'.format(self.name,self.color,self.height,self.weight)
    
    def bark(self):
        super().bark()   #调用父类的bark方法
        print('嘤嘤嘤')
        pass
    pass

kj=keji('柯基犬','红色')
kj.bark()
print(kj)

#多态：就是同一种行为，对于不同的子类【对象】有不同的行为表现
#前提条件：1、继承：多态必须发生在父类和子类之间；2、重写：子类重写父类的方法

class Animal:
    def say(self):
        print("我说话")
        pass
    pass

class Duck(Animal):
    def say(self):
        super().say()
        print('嘎嘎嘎')
        pass
    pass

class Dog(Animal):
    def say(self):
        super().say()
        print('汪汪汪')
        pass
    pass

class Cat(Animal):
    def say(self):
        super().say()
        print('喵喵喵')
        pass
    pass

class People:
    def say(self):
        print('我是人类')
        pass
    pass

class Student(People):
    def say(self):
        super().say()
        print('我是一年级的小明')
        pass
    pass

def commonInvoke(obj):
    obj.say()
    
duck=Duck()
duck.say()
# Duck().say()
dog=Dog()
dog.say()

listObj=[Duck(),Dog(),Cat(),Student()]  #此处也能打印出Student的相关信息
for item in listObj:
    commonInvoke(item)
    
#多态：可以增加程序的灵活性，扩展性，弱类型语言，不需要指定类型
#鸭子类型：是动态类型的一种风格，一个对象有效的语义，不是由继承自特定的类或实现特定的接口，而是由当前方法和属性的集合决定的。
#在鸭子类型中，关注的不是对象的类型本身，而是它是如何使用的
    

#属性：类属性和实例属性
#类属性：就是类对象所拥有的属性
class Student:
    name='Liuming' # 属于类属性，就是Student类对象所拥有的
    def __init__(self,age):
        self.age=age  # 实例属性
        pass
    pass

lm=Student(20)   #创建实例对象lm
print(lm.age)    # 结果：20
print(lm.name)   #通过实例对象去访问类属性  结果：Liuming
lm.name='刘德华'  #通过实例对象，不能对类属性进行修改，只会增添
print(lm.name)   #结果：刘德华
print(Student.name)  #结果：Liuming
Student.name='李易峰' #此处可以修改，只能通过类对象进行修改
print(Student.name)  #结果：李易峰
#print(Studnet.age)  #此处报错，无法访问，类对象不可以访问实例属性

#类属性是可以被类对象和实例对象共同访问使用的；实例属性只能由实例对象所访问
#所有实例对象的类对象指针指向同一类对象，实例属性在每个实例中独有一份，而类属性是所有实例对象共有一份

#类方法：
class People:
    country='China'
    
    @classmethod     #类方法，用classmethod来进行修饰
    def get_country(cls):
        return cls.country  #访问类属性
        pass
    pass

    @classmethod
    def change_country(cls,data): #类方法
        cls.country=data  #修改类属性的值，在类方法中
        pass
    pass

    @staticmethod
    def getData():
        return People.country  #通过类对象去引用
        pass
    
print(People.getData())      #静态方法，结果：China
print(People.get_country())  #通过类对象直接引用
p=People()  #创建一个实例对象
print(p.getData())  #一般不会通过实例对象去访问静态方法
print('实例对象访问 %s'%p.get_country())
print('实例对象访问 {}'.format(p.get_country()))
People.change_country('英国')
print('实例对象访问 %s'%p.get_country())

#静态方法：类对象所拥有的方法，需要用@staticmethod来表示静态方法，静态方法不需要任何参数
#由于静态方法主要来存放逻辑性的代码，本身和类以及实例对象没有交互；在静态方法中，不会涉及到类中方法和属性的操作

import time
class TimeTest:
    def __init__(self,hour,min,second):
        self.hour=hour
        self.min=min
        self.second=second

    @staticmethod
    def showTime():
        return time.strftime("%H:%M:%S",time.localtime())
        pass
    pass

print(TimeTest.showTime())
t=TimeTest(2,10,23)
print(t.showTime())  #返回的仍是当前时间

#从方法的形式可以看出，类方法的第一个参数是类对象cls进而去引用类对象的属性和方法，必须用装饰器@classmethod来修饰
#实例方法的第一个参数必须是self,通过这个self可以去引用类属性或者实例属性，若存在相同名称实例属性和类属性的话，实例属性的优先级最高
#静态方法不需要定义额外的参数，若是要引用属性的话，则可以通过类对象或者是实例对象去引用即可，必须用装饰器@staticmethod来修饰
