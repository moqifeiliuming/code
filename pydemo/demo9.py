#私有化属性：为了更好的保存属性安全，不能随意修改，将属性定义为私有属性，添加一个可调用的方法去访问
#语法：两个下划线开头(__)，声明该属性为私有，不能在类的外部被使用或直接访问
#使用私有属性的场景：
#1、把特定的一个属性隐藏起来，不想让类的外部直接进行调用
#2、想保护该属性，不想让属性的值随意的改变
#3、保护这个属性，不想让派生类【子类】去继承

class Person:
    
    __hobby='sing'
    def __init__(self):
        self.__name='liuming' #加两个下划线，将此属性私有化,不能在外部直接访问
        self.age=30
        pass

    def __str__(self):
        return '{}的年龄是{}，兴趣爱好是{}'.format(self.__name,self.age,self.__hobby)

    def changeValue(self):
        Person.__hobby='dancing'
        pass

    def __str__(self):
        return '{}的年龄是{}，兴趣爱好是{}'.format(self.__name,self.age,self.__hobby)

xm=Person()
#print(xm.__name)  # 通过类对象，在外部访问的,不能访问私有属性
print(xm)
xm.changeValue()
print(xm)

#小结：1、私有化的【实例、类】属性，不能在外部直接访问，可以在类的内部随意的使用
#2、子类不能继承父类的私有化属性【只能继承父类公共的属性和行为】
#3、在属性名的前面直接加 __ 就可以变为私有化

class Animal:
    def __eat(self):
        print('吃东西')
        pass
    def run(self):
        self.__eat()
        print('飞快跑')
    pass

class Bird(Animal):
    pass

bird=Bird()
# bird.eat()  子类不能集成父类的私有化方法
bird.run()    #结果：吃东西     飞快跑

#特性：私有化方法一般是类内部调用，子类不能继承，外部不能调用
#Property属性  类属性：即在类中定义值为property对象的类属性；装饰器：即在方法上使用装饰器
class Person:
    def __init__(self):
        self.__age=18

    def get_age(self):
        return self.__age

    def set_age(self,age):
        if age<0:
            print('年龄不能小于0')
        else:
            self.__age=age
            pass

    #实现方式1：定义一个类属性，实现通过直接访问属性的形式去访问私有属性
    age=property(get_age,set_age)
    pass

    #实现方式2  通过装饰器的方式去声明
    @property  #添加属性标志，提供一个getter方法
    def age(self):
        return self.__age

    @age.setter  #提供一个setter方法
    def age(self,parms):
        if parms<0:
            print('年龄不能小于0')
        else:
            self.__age=parms
            pass
        
p1=Person()
print(p1.age)
p1.age=23
print(p1.age)
# p1.get_age()
# p1.set_age()

class Animal:
    def __init__(self):
        self.color='红色'
        pass
    pass

    def __new__(cls,*args,**kwargs):
        return super().__new__(cls,*args,**kwargs)
        return Object.__new__(cls,*args,**kwargs)
    pass

tigger=Animal()  #实例化的过程会自动调用__new__去创建
#在新式类中 __new__ 才是真正的实例化的方法，为类提供外壳制造出实例框架，然后调用该框架内的构造方法__init__进行操作

#单例模式  目的：确保某一个类只有一个实例存在
class DataBase:
    def __new__(cls,*args,**kwargs):
        #cls._instance=cls.__new__(cls) 不能使用自身的new方法，容易造成一个深度递归循环
        if not hasattr(cls,'_instance'):  #如果不存在就开始创建
            cls._instance=super().__new__(cls,*args,**kwargs)
        return cls._instance
    pass

data1=DataBase()
print(id(data1))
data2=DataBase()
print(id(data2))
#结果：二者id号一样

#异常处理  except在捕获错误异常的时候，是要根据具体的错误类型来捕获的
#用一个块，可以捕获多个异常  Exception可以捕获所有的异常

try:
    print(b)
    pass
except NameError as msg:
    print(msg)
    pass
print("初始化")

#不需要在每个可能出错的地方去捕获，只要在合适的层次去捕获错误就可以
#异常的抛出机制：如果在运行时发生异常，解释器会查找相应的异常捕获类型；如果在当前函数没有找到的话，会将异常传递给上层的调用函数，看能否处理
#如果在最外层没有找到的话，解释器就会退出

try:
    #a=1
    print(a)
    pass
except Exception as msg:
    print(msg)
    pass
else:
    print("继续执行")
    pass
finally:  #无论是否发生异常，都会执行
    print("结束程序")
    pass


class ToolongMyException(Exception):
    def __init__(self,leng):
        self.leng=leng
        pass

    def __str__(self):
        return '您输入姓名数据长度是'+str(self.leng)+'：超过长度了'
    pass

def name_Test():
    name=input("请输入姓名：")
    try:
        if len(name)>=5:
            raise ToolongMyException(len(name))
        else:
            print(name)
            pass
        pass
    except ToolongMyException as result:
        print(result)
        pass
    finally:
        print("执行完毕了")

name_Test()

class Student:
    def __init__(self):
        pass
    pass
#动态添加方法：给类绑定类方法和静态方法

import types  #添加方法
def dymicMethod(self):
    print('{}的体重是：{}kg 在{}读大学'.format(self.name,self.weight,Student.school))
    pass

@classmethod
def classTest(cls):  # 类方法
    print('这是一个类方法')
    pass

@staticmethod  # 静态方法
def staticMethodTest():
    print('这是一个静态方法')
    pass

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    pass

    def __str__(self):
        return '{}今天{}岁了'.format(self.name,self.age)
    pass

print('绑定类方法')
#Student.TestMethod=classTest
#Student.TestMethod()

Student.classTest=classTest
Student.classTest()

Student.staticMethodTest=staticMethodTest
Student.staticMethodTest()
print('------------------绑定类方法执行结束------------------')

zyh=Student('张艳华',20)
zyh.weight=50   #动态添加
zyh.printInfo=types.MethodType(dymicMethod,zyh)  #动态的绑定方法
#zyh.TestMethod()
zyh.classTest()
print('------------------实例对象调用  动态绑定类方法------------------')

print(zyh)
print(zyh.weight)
print('---------------另外一个实例对象  张明----------------')
zm=Student('张明',20)
zm.weight=80  #动态增加
print(zm)

zm.printInfo=types.MethodType(dymicMethod,zm) #动态的绑定方法
#print(zm.weight)
print('-----------------------给类对象添加属性---------------')
Student.school='北京邮电大学'  #动态添加类属性
print(zm.school)
print('------------------执行动态调用实例方法-----------------')
zyh.printInfo()   #调用动态绑定的方法
zm.printInfo()


#只有在__slots__变量中的属性才能被添加，没有在__slots__变量中的属性会添加失败。__slots__属性子类不会继承，只有在当前类中有效
#1、限制要添加的实例属性；2、节约内存空间
class Student:
    __slots__=('name','age')
    
    def __str__(self):
        return '{}.......{}'.format(self.name,self.age)
    pass

xw=Student()
xw.name='小王'
xw.age=20
#xw.pro='arm'   #用了__slots__函数，则不能添加其他的属性
print(xw)
#print(xw.__dict__) #所有可以用的属性都在这里存储，不足点：占用的内存空间大

#在继承关系中的使用  __slots__
#子类未声明 __slots__时，是不会继承父类的__slots__,此时子类是可以随意的进行属性赋值的
#子类声明了 __slots__时，继承父类的__slots__，也就是子类__slots__的范围是为其自身+父类的__slots__
class subStudent(Student):
    #__slots__=()
    __slots__=('gender','pro')  #此时不需要再写'name','age'（已拥有）,再写的话就占用了内存空间
    pass

ln=subStudent()
ln.gender='男'
ln.pro='计算机信息管理'
ln.name='liuming'
print(ln.gender,ln.pro,ln.name)


#1、Python中new方法作用是什么?
#用来创建实例对象，只有继承了Object的话，才有该方法

#2、什么是单例模式? 单例模式适用于什么场景?
#一个类有且只有一个实例，并且提供了一个全局的访问点
#场景：日志插入logger的操作，网站计数器，权限验证模块，Windows资源管理器，系统回收站，数据库连接池

#3、私有化方法与私有化属性在子类中能否继承?
#不能

#4、在Python中什么是异常?
#程序在执行的过程中发生的错误

#5、Python中是如何处理异常的。
#分别根据异常的类型进行处理

#6、Python中异常处理语句的一般格式，可以使用伪代码的形式描述。
#try：
#   正常操作
#except:
    #.....
#else:
    #.....
#finally:
    #.....

#7、_slots_属性的作用
#限制属性的随意输入；节省内存空间 __dict__

#8、私有化属性的作用?
#保护数据，封装性的体现

#9、在类外面是否能修改私有属性。
#不可以直接修改，可通过方法去实现，还可以借助属性函数property去实现

#10、如果一个类中，只有指定的属性或者方法能被外部修改。那么该如何限制外部修改。
#对属性进行私有化的设定

#1、编写一段代码以完成下面的要求
#·定义一个Person类,类中要有初始化方法,方法中要有人的姓名,年龄两个私有属性.·提供获取用户信息的函数.
#·提供获取私有属性的方法，提供可以设置私有属性的方法.
#·设置年龄的范围在(0-120)的方法，如果不在这个范围，不能设置成功.

class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
        pass
    pass

    def __str__(self):
        return '{}的年龄是:{}岁'.format(self.__name,self.__age)
    pass

    def getAgeInfo(self):
        return self.__age

    def getNameInfo(self):
        return self.__name

    def setAge(self,age):
        if 0 < age  and age < 120:
            self.__age=age
        else:
            print('您输入的年龄不合法')
            pass
        pass

    def setName(self,name):
        self.__name=name
  
    
#2、请写一个单例模式
class DataBase:
    def __new__(cls,*args,**kwargs):
        if not hasattr(cls,'_instance'):  #如果不存在就开始创建
            cls._instance=super().__new__(cls,*args,**kwargs)
        return cls._instance
    pass

# 3、创建一个类，并定义两个私有化属性，提供一个获取属性的方法，和设置属性的方法。利用property属性给调用者提供属性方式的调用获取和设置私有属性方法的方式。
class Student:
    def __init(self):
        self.__name='张三'
        self.__age=20
        pass
    pass

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name=name

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,age):
        self.__age=age

    def __str__(self):
        return self.__name

    def __call__(self,*args,**kwargs):
        #print(self.__name+'的年龄为：'+str(self.__age))
        #print('{}的年龄是：{}'.format(self.__name,self.__age))
        pass
    pass

xw=Student()
xw() #将实例对象以函数的形式去调用
#print(xw)
    
#4、创建一个Animal类，实例化一个cat对象，请给cat对象动态绑定一个run方法，给类绑定一个类属性colour，给类绑定一个类方法打印字符串'ok'。
import types
def run(self):
    print('跑到很远')

@classmethod  #类方法
def info(cls):
    print('ok')
    pass

class Animal:
    pass

Animal.color='黑色'
Animal.info=info
cat=Animal()
cat.run=types.MethodType(run,cat)  #动态绑定
cat.run()
print(cat.color)
Animal.info()

import types
def run(self):
    print("跑的很快")
    pass

@classmethod
def pdf(cls):
    print('ok')
    pass

class Animal:
    pass

Animal.colour='白色'
Animal.pdf=pdf
cat=Animal()
cat.run=types.MethodType(run,cat)
cat.run()
print(cat.colour)
Animal.pdf()
