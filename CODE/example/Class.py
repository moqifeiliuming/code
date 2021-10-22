# __init__()方法，是一个特殊的方法，类似Java预言中的构造方法，该方法中必须包括一个self参数，且为第一个参数。
# self参数是一个指向实例本身的引用，用于访问类中的属性和方法。
class Geese:
    def __init__(self):
        print("我是大雁")
geese = Geese()

# 类的成员主要由实例方法和数据成员组成，实例方法是指在类中定义的函数，该函数是一种在类的实例上操作的函数
# 函数实现的是某个独立的功能，而实例方法是实现类中的一个行为，是类的一部分

class Geese:
    def __init__(self,beak,wing,claw):
        print("我是大雁类")
        print(beak)
        print(wing)
        print(claw)
    def fly(self,state):
        print(state)
beak='喙很高'
wing='翅膀长'
claw='爪子尖'
print()
geese=Geese(beak,wing,claw)
geese.fly("我飞行的时候呈现人字形")

# 在创建实例方法时，也可以为参数设置默认值，但是被设置了默认值的参数必须位于所有参数的最后(即最右侧)
# def fly(self,state='我会飞行'):
# 类属性是指在类中，并且在函数体外的属性。类属性可以在类的所有实例之间共享值，也就是在所有实例化的对象中公用。
# Python除了可以通过类名称访问类属性，还可以动态地为类和对象添加属性
# 实例属性只能通过实例名访问，如果通过类名进行访问时，会发生错误
# 对于实例属性可以通过实例名称进行修改，与类属性不同，通过实例名称修改实例属性后，并不影响该类的另一个实例中相应的实例属性的值

# 访问限制
# 以单下划线开头的表示protected（保护）类型的成员，只允许类本身和子类进行访问，保护属性可以通过实例名进行访问，但不能使用"from module import*"语句导入
class Swan:
    _neck_swan='天鹅的脖子很长'
    def __init__(self):
        neck_swan='咕咕咕'
        # print(Swan.neck_swan)  # 实例属性不能通过类名来访问
        print('__init__()：',Swan._neck_swan)
#Swan()  # 结果：天鹅的脖子很长
swan = Swan()
print("直接访问：",swan._neck_swan)

# 双下划线private（私有）类型的成员，只允许定义该方法的类本身进行访问，而且也不能通过类的实例进行访问，但是可以通过“类的实例名._类名__xx”方式进行访问
class Swan:
    __neck_swan='天鹅的脖子很长'
    def __init__(self):
        print('__init__()：',Swan.__neck_swan)  #结果：__init__()： 天鹅的脖子很长
#Swan()  # 结果：天鹅的脖子很长
swan = Swan()
print("加入类名：",swan._Swan__neck_swan)  #结果：加入类名： 天鹅的脖子很长
# print("直接访问：",swan.__neck_swan)  # 报错，私有属性不能直接通过实例名+属性名访问，可以在类的实例方法中访问，或者通过“类的实例名._类名__xx”方式进行访问

# @property(装饰器)将一个方法转换为属性，从而实现用于计算的属性。将方法转换为属性后，可以直接通过方法名来访问方法，无需在添加小括号()
class Rect:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    @property
    def area(self):
        return self.width * self.height
rect = Rect(25,25)
print("面积为：",rect.area)  # 此时实例调用为rect.area，而不是rect.area()
rect = Rect(20,20)

# 如果想要限制创建的类属性或实例不能在类体外修改，可以将其设置为私有的，但设置W为私有后，在类体外也不能获取它的值
# 如果想要创建一个可以读取但不能修改的属性，可以使用@Property实现只读属性；通过属性不仅可以将属性设置为只读属性，
# 而且可以为属性设置拦截器，即允许对属性进行修改，但修改时需要遵守一定的约束
class TVshow:
    list_film = ['战狼2','红海行动','西游记女儿国']
    def __init__(self,show):
        self.__show = show
    @property                   #将方法转换为属性
    def show(self):
        return self.__show
    @show.setter                #设置setter方法，让属性可修改
    def show(self,value):
        if value in TVshow.list_film:
            self.__show = "您选择了《"+value+"》，稍后将播放"
        else:
            self.__show = "您点播的不存在"
tvshow = TVshow("战狼2")
# print("正在播放：《"+tvshow.show+"》")
print("正在播放：《",tvshow.show,"》")  #此种输出形式比上面的好一些，不要考虑相连之间的类型是否一致
print("您可以从：",tvshow.list_film,"中选择您喜欢看的电影")
tvshow.show = "红海行动"
print(tvshow.show)

# 在面向对象编程中，被继承的类成为父类或者基类，新的类成为子类或者派生类
# 基类的成员都会被派生类继承，当基类中的某个方法不完全适应与派生类是，就需要在派生类中重写父类的这个方法
# 派生类中调用基类的__init__()方法时，不会自动调用基类的__init__()方法，需要进行初始化，在派生类使用super()函数，super().__init__()


