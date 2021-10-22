def function_tips():
    import datetime
    mot=['1',
         '2',
         '3',
         '4',
         '5',
         '6',
         '7'
    ]
    day = datetime.datetime.now().weekday()   #输出今天是周几
    print(mot[day])
function_tips()

#形式参数：在定义函数时，函数名后面括号中的参数为“形式参数”
#实际参数：在调用一个函数时，函数名后面括号中的参数为“实际参数”，也就是将函数的调用者提供给函数的参数称为实际参数。
#当实际参数为不可变对象时，进行值传递；当实际参数为可变对象时，进行的是引用传递
#值传递和引用传递的基本区别：进行值传递后，改变形式参数的值，实际参数的值不变；而进行引用传递后，改变形式参数的值，实际参数的值也一同改变

def fun_bmi(person,height,weight):
    print(person+"的身高："+str(height)+"米\t体重："+str(weight)+"千克")
    bmi = weight / (height * height)
    print(person+"的BMI指数为："+str(bmi))
    if bmi < 18.5:
        print("您的体重过轻")
    if 18.5 <= bmi < 24.9:
        print("您的体重正常")
    if 24.9 <= bmi < 29.9:
        print("您的体重偏胖")
    if bmi >= 29.9:
        print("您的体重肥胖")
fun_bmi("liuming",1.71,76)
fun_bmi("xiongchen",1.63,56)

#关键词参数是指使用形式参数的名字来确定输入的参数值，此时不需要与形式参数的位置完全一致，只需将参数名写正确即可
#fun_bmi(height = 1.83, weight = 60, person = "liuming")
#在Python中，可以使用“函数名._defaults_"查看函数的默认值参数的当前值，其结果是一个元祖。使用”fun_bmi._defaults_"时，结果为："('liuming',)"
#定义函数时，为形式参数设置默认值要牢记一点：默认参数必须指向不可变对象
def demo(obj=None):
    if obj==None:
        obj=[]
    print("obj的值：",obj)
    obj.append(1)
demo()
demo()

#可变参数：主要两种形式：一种是 *parameter，另一种是 **parameter
# *parameter：表示接收任意多个实际参数并将其放到一个元组中
def printcoffee(*coffeename):
    print('\n我喜欢的咖啡有：')
    for item in coffeename:
        print(item)
printcoffee('蓝山')
printcoffee('蓝山','卡布奇诺','土耳其')
printcoffee('蓝山','卡布奇诺','摩卡')
# printcoffee(['蓝山','卡布奇诺','土耳其'])   结果为：我喜欢的咖啡有：['蓝山', '卡布奇诺', '土耳其']
#如果想要使用一个已经存在的列表作为函数的可变参数，可以在列表的名称前加"*"
param=['蓝山','卡布奇诺','土耳其']
printcoffee(*param)

# **parameter：表示接受任意多个类似关键字参数一样显示赋值的实际参数，并将其放到一个字典中
def printsign(**sign):
    print()
    for key,value in sign.items():
        print('['+key+'] 的星座是：'+ value)
printsign(绮梦='水瓶座',冷衣='射手座')
printsign(香凝='双鱼座',黛蓝='双子座',刘明='天秤座')
# 如果想要使用一个已经存在的字典作为函数的可变参数，可以在字典的名称前加“**”
dict1={'绮梦':'水瓶座','香凝':'双鱼座'}
printsign(**dict1)

# 如果返回一个值，那result中保存就是返回的一个值，该值可以为任何类型；如果返回多个值，那result中保存的是一个元组
def fun_checkout(money):
    money_old = sum(money)
    money_new = money_old
    if 500 <= money_old < 1000:
        money_new = '{:.2f}'.format(money_old * 0.9)
    elif 1000 <= money_old < 2000:
        money_new = '{:.2f}'.format(money_old * 0.8)
    elif 2000 <= money_old < 3000:
        money_new = '{:.2f}'.format(money_old * 0.7)
    elif money_old >= 3000:
        money_new = '{:.2f}'.format(money_old * 0.6)
    return money_old,money_new
print("现在开始计算\n")
money_list = []
while True:
    inputmoney = float(input("请输入商品金额(输入0为结束)："))
    if int(inputmoney) == 0:
        break
    else:
        money_list.append(inputmoney)
money = fun_checkout(money_list)
print("合计金额为：{}  应付金额为：{}".format(money[0],money[1]))

#局部变量：指的是在函数内部定义并使用的变量，只在函数内部有效；在函数运行时才会创建，在函数运行之前或者运行完毕之后，所有的名字不存在
mess = '1'
def demo():
    mess = '2'
    print(mess)  #结果：2
demo()
print(mess) #结果：1

#在函数体内定义，并且使用global关键字修饰后，该变量变为全局变量，在函数体外也能访问到改变量，并且在函数体内还可以对其进行修改
mess = '1'
print(mess)    #结果：1
def demo():
    global mess
    mess = '2'
    print(mess)  #结果：2
demo()
print(mess)   #结果：2

#匿名函数：指没有名字的函数，应用在需要一个函数，但是又不想费神去命名这个函数的场合，通常情况下，这样的函数只使用一次
#使用lambda表达式时，参数可以有多个，用逗号","分隔，但表示式只能有一个，即只能返回一个值，并且不能出现其他非表达式语句(如for或者while)
import math
r = 10
result = lambda r:math.pi*r*r
print("半径",r,'的圆形面积为：',result(r))
# 在使用lambda表达式时，需要定义一个变量，用于调用该lambda表达式，否则出现 <function <lambda> at 0x0000016885F004C0>

bookinfo = [('不一样的卡梅拉',22.5,120),('零基础学android',65.1,89),('摆渡人',23.4,65)]
print('爬取到的商品信息：\n',bookinfo,'\n')
bookinfo.sort(key=lambda x:(x[1],x[1]/x[2]))  #按指定规则进行排序
print("排序后的商品信息：\n",bookinfo)
