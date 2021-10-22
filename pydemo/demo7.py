#面向过程：根据业务逻辑从上到下写代码
#函数式：将某功能代码封装到函数中，日后便无需重复编写，仅调用函数即可
#面向对象编程：将数据与函数绑定在一起，进行封装，这样能够更快速的开发程序，减少重复代码的重写过程

class Person:
    name='小明'   #类属性
    age=20       #类属性
    def eat(self):   #实例方法  self相当于默认参数
        print('大口吃饭')
        pass
    def run(self):
        print('飞速的跑')

    def __init__(self):   #实例属性
        self.name='小明'

xm=Person()  #创建对象
print(xm.age)
print("{}的年龄是：{}".format(xm.name,xm.age))
xm.run()   #调用函数   实例方法

class Person:
    name = '小米'
    age = 23
    def eat(self):
        print("吃的很饱")
    def run(self):
        print("跑的很快")
    def __init__(self):
        self.name = '李华'
people = Person()
print(people.name)
print(people.age)
print("{}的年龄是：{}".format(people.name,people.age))
people.run()

#实例方法：在类的内部，使用def关键字可以定义一个实例方法，与一般函数定义不同，类方法必须包括参数self或者其他名字，且为第一个参数。
#属性：类里面定义的变量。定义在类里面，方法外面的属性称之为类属性，定义在方法里面使用self引用的属性称为实例属性

class People:
    def eat(self):
        print('喜欢吃榴莲')
    pass
xq=People()
xq.name='小倩'   #实例属性
xq.sex='女生'    #实例属性
xq.age=20       #实例属性
xq.eat()
print(xq.name,xq.sex,xq.age)

xl=People()
xl.name='小丽'   #实例属性
xl.sex='女生'    #实例属性
xl.age=21       #实例属性
xl.eat()
print(xl.name,xl.sex,xl.age)

#__init__(self)方法：初始化方法，实例化对象的时候自动调用，完成一些初始化设置
class People:
    def __init__(self):   #默认被调用，自动调用
        self.name='小倩'
        self.sex='女生'
        self.age=20
        pass
        
    def eat(self):
        print('喜欢吃榴莲')  
    pass

xq=People()
xq.name='小倩'   #实例属性
xq.sex='女生'    #实例属性
xq.age=20        #实例属性
xq.eat()
print(xq.name,xq.sex,xq.age)

class Person:
    def __init__(self,name,sex,age):
        self.name=name
        self.sex=sex
        self.age=age
        pass

    def eat(self,food):
        print(self.name+"喜欢吃"+food)
        
zp=Person('张鹏','男生',20)
print(zp.name,zp.sex,zp.age)
zp.eat('香蕉')
print('{}是{}，年龄：{}'.format(zp.name,zp.sex,zp.age))

#总结 __init__
#1、python自带的内置函数，具有特殊的函数，使用双下划线包起来的魔术方法
#2、是一个初始化的方法，用来定义实例属性和初始化数据的，在创建对象的时候自动调用不用手动去调用
#3、利用传参的机制可以让我们定义功能更加强大并且方便的类

#self：self和对象指向同一个内存地址，可以认为self就是对象的引用
#特点：self只有在类中定义，实例方法的时候才有意义，在调用时候不必传入相应的参数，而是由解释器自动去指向
#self的名字是可以更改的，可以定义成其他的名字，只是约定俗成的定义为了self
#self指的是类实例对象本身，相当于java中的this

class Person:
    def eat(self,name,food):
        print('%s喜欢吃%s'%(name,food))
        pass
    pass
xw=Person()
print('xw = %s',id(xw))
xw.eat('小王','榴莲')

#魔术方法：有些内置好的特定方法  __init__     __str__   __new__  等等
#在进行特定的操作时会被自动调用

class Person:
    def __init__(self,pro,name,food):
        self.pro=pro
        self.name=name
        self.food=food
        print("--------init-------函数执行")
        pass

    # def eat(self,name,food):
    #     print('%s喜欢吃%s修的专业是：%s'%(self.name,self.food,self.pro))
    #     pass

    def __str__(self):   #能使xw的对象值打印出来
        return '%s喜欢吃%s修的专业是：%s'%(self.name,self.food,self.pro)
        pass

    def __new__(cls,*args,**kwargs):
        print('-------new-------函数的执行')  #首先执行，如果创建了对象，则返回执行__init__函数
        return object.__new__(cls)  #cls代表当前的对象
        pass
    pass

xw=Person('心理学','小王','榴莲')
print(xw)

#重点
#__new__和__init__函数的区别
#__new__类的实例化方法，必须要返回该实例，否则对象就创建不成功
#__init__用来做数据属性的初始化工作，也可以认为是实例的构造方法，接受类的实例self并对其进行构造
#__new__ 至少有一个参数是cls代表要实例化的类，此参数在实例化时由python解释器自动提供
#__new__ 函数执行要早于__init__函数

#决战紫禁之巅
import time  #导入time包
class Role:
    def __init__(self,name,hp):
        self.name=name
        self.hp=hp
        pass

    def tong(self,enemy):  #捅刀
        enemy.hp-=10
        info='【%s】捅了【%s】一刀'%(self.name,enemy.name)
        print(info)
        pass

    def kanren(self,enemy): #砍人
        enemy.hp-=15
        info='【%s】砍了【%s】一刀'%(self.name,enemy.name)
        print(info)
        pass

    def chiyao(self):   #吃药
        self.hp+=10
        info='【%s】吃了一颗补血药，增加了10滴血'%(self.name)
        print(info)

    def __str__(self):
        return '%s 还剩下%s 的血量'%(self.name,self.hp)

xmcx=Role('西门吹雪',100)
ygc=Role('叶孤城',100)

while True:
    if xmcx.hp<=0 or ygc.hp<=0:
        break
    xmcx.tong(ygc)
    print(xmcx)
    print(ygc)
    print('----------------------------')
    ygc.kanren(xmcx)
    xmcx.chiyao()
    xmcx.tong(ygc)
    print(xmcx)
    print(ygc)
    print('----------------------------')
    ygc.chiyao()
    ygc.tong(xmcx)
    print(xmcx)
    print(ygc)
    time.sleep(1)

print('对战结束')

# import time
# class game:
#     def __init__(self,name,hp):
#         self.name=name
#         self.hp=hp
#         pass
#     def tong(self,enemy):
#         enemy.hp-=10
#         print("%s捅了%s一刀"%(self.name,enemy.name))
#     def kan(self,enemy):
#         enemy.hp-=15
#         print("%s砍了%s一刀"%(self.name,enemy.name))
#     def chiyao(self):
#         self.hp+=20
#         print("%s吃了一颗药"%(self.name))
#     def __str__(self):
#         return "%s还剩下血量为%s"%(self.name,self.hp)
#
# liu=game("liu",100)
# ming=game("ming",100)
# while True:
#     if liu.hp <= 0 or ming.hp <= 0:
#         break
#     liu.tong(ming)
#     liu.kan(ming)
#     liu.chiyao()
#     print(liu)
#     print(ming)
# print("对战结束")

#请编写代码，验证self就是实例本身   
class Person:
    def weight(self):
        print('self=%s'%id(self))
    pass
liming=Person()
liming.weight()
print(id(liming))
#二者的地址是一样的，所以可以验证

class Person:
    def weight(self):
        print('self=%s'%id(self))
    pass
xm = Person()
xm.weight()
print(id(xm))
