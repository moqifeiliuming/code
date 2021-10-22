#函数：一系列Pyhon语句的组合，可以在程序中运行一次或者多次，一般是完成具体的独立功能
#为什么要使用函数：代码的复用最大化以及最小化冗余代码,整体代码结构清晰，问题局部化
# def 函数名():
#    函数体[一系列的Pyhon语句，表示独立的功能]
#函数的调用：
#    本质上就是去执行函数定义里面的代码块，在调用函数之前，必须先定义

# print("小张的身高是%f"%1.73)
# print("小张的体重是%f"%160)
# print("小张的爱好是%s"%'打排球')

def printInfo():
    #代码块
    print("小张的身高是%f"%1.73)
    print("小张的体重是%f"%160)
    print("小张的爱好是%s"%'打排球')
    pass
#函数的调用
printInfo()
print("---------------------")

def printInfo(name,height,weight,hobby):
    #代码块
    print("%s的身高是%f"%(name,height))
    print("%s的体重是%f"%(name,weight))
    print("%s的爱好是%s"%(name,hobby))
    pass
#函数的调用
printInfo('小明',180,190,'打篮球')
print()

#必选参数
def sum(a,b):  #形式参数，不占内存地址
    sum = a+b
    print(sum)
    pass
sum(20,10)  #实际参数，占用内存地址

#默认参数
def sum1(a=20,b=20):
    print('默认参数使用结果=%d'%(a+b))
    pass
sum1(10) # 默认给第一个参数   结果为：30
sum1(10,50)  # 结果为：60
sum1()   # 结果为：40

# 可变参数
def getComputer(*args): # 可变长的参数，接收的是元组类型
    print(args)
    pass
getComputer(1)
getComputer(1,2,3,4)
getComputer(1,4,'liuming')

def gets(*args):
    print(args)
    pass
gets(1,2,3)
gets(1,2,'liuming')
gets(1,2,[2,3],'liuming')

# **（关键字）来定义
# 在函数体内  参数关键字是一个字典类型  key是一个字符串
def keyFunc(**kwargs):
    print(kwargs)
    pass
# keyFunc(1,2,3) # 不可以传递的
dictA={"name":'leo',"age":35}
keyFunc(**dictA)  #可以传递
keyFunc(name='peter',age=26)  #结果为：{'name': 'peter','age': 26}
keyFunc()   #结果为{}

def complexFunc(*args,**kwargs):
    print(args,end=' ')
    print(kwargs)
    pass
complexFunc()  #结果为() {}  不会报错
complexFunc(1,2,3,4)  #结果为(1,2,3,4) {}
complexFunc(1,2,3,4,name='liuming')  #(1, 2, 3, 4) {'name': 'liuming'}
complexFunc(age=36) #结果为：()  {'age': 36}
#可选参数必须要在关键字可选参数前面
#可选参数：接受的数据是一个元组类型
#关键字可选参数：接受的数据是一个字典类型

#函数返回值
#概念：函数执行完会返回一个对象，如果在函数的内部有return就可以返回实际的值，返回None
#类型：可以返回任意类型，返回值类型应取决于return后面的类型
#在一个函数体内可以出现过个return值，但是肯定只能返回一个return
#如果在一个函数体内，执行了return，意味着函数就执行完成退出了，return后面的代码语句将不会执行
def sum(a,b):
    sum=a+b
    return sum  #将计算的结果返回
    pass
k=sum(20,20)
print(k)    # return能够返回sum的值，但是缺少print(k)是不能显示K的值

def calComputer(num):
    result=0
    i=1
    while i<=num:
        result+=i
        i+=1
        pass
    return result
    pass
value=calComputer(10)
print(type(value))  # <class 'int'>
print(value)        # 55

def calComputer(num):
    li=[]
    result=0
    i=1
    while i<=num:
        result+=i
        i+=1
        pass
    li.append(result)
    return li
    pass
value=calComputer(10)
print(type(value))    #<class 'list'>
print(value)          #[55]

#写函数，接收n个数字，求这些参数数字和
def sumFunc(*args):
    result = 0
    for item in args:
        result+=item
        pass
    return result
    pass
value=sumFunc(1,2,3,4,5)
print('value={0}'.format(value)) #format格式化输出
print(type(value))
print(value)

#写函数，找出传入的列表或元组的奇数位对应的元素，并返回一个新的列表
def process_Func(con):
    listNew=[]
    index=1
    for item in con:
        if index % 2 == 1:
           listNew.append(item) 
           pass
        index+=1
        pass
    return listNew
    pass
rs=process_Func([1,2,3,4,5,6])
print(rs)
print(type(rs))

#写函数，检查传入字典的每一个value的长度；如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者
#字典中的value只能是字符串或者列表
def dictFunc(kwargs):  # **kwargs
    result={}
    for key,value in kwargs.items():
        if len(value)>2:
            result[key]=value[:2]#向字典中去添加数据
            pass
        else:
           result[key]=value
           pass
        pass
    return result
    pass
dictObj={'name':'liuming','hobby':['sing','dancing','coding'],'pro':'arm'}
print(dictFunc(dictObj))

def dic(kwargs):
    result = {}
    for key,value in kwargs.items():
        if len(value) > 2:
            result[key] = value[:2]
        else:
            result[key] = value
    return result
print(dictFunc({'name':'liuming','hobby':['sing','dancing','coding'],'pro':'arm'}))
