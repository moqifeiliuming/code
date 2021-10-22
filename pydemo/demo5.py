#当全局变量和局部变量出现重复定义的时候，程序会优先执行函数内部定义的变量
#如果在函数的内部要想对全局变量进行修改的话，必须用global关键字就行声明
def printInfo():
    name='peter'
    pass
print()

list1 = [1,2,3,4]
str1 = "hello world"
def fun():
    list1 = [5,6,7,8]
    str1 = "世界，你好"
    print(list1)
    print(str1)
fun()
print(list1)
print(str1)

# 使用global来改变外部变量
list1 = [1,2,3,4]
str1 = "hello world"
def fun():
    global list1,str1
    list1 = [5,6,7,8]
    str1 = "世界，你好"
    print(list1)
    print(str1)
fun()
print(list1)
print(str1)

#不可变类型
a=1
def func(x):
    print('X的地址:{}'.format(id(x)))
    x=2
    print('X修改后的地址:{}'.format(id(x)))
    print(x)
    pass
print('a的地址为:{}'.format(id(a)))
func(a)
print(a)
print('a的地址为:{}'.format(id(a)))

#可变类型
li=[23]
def testRenc(parms):
    li.append([1,2,3])
    print(id(parms))
    pass
print(id(li))
testRenc(li)

#小结：1、在python当中，万物皆对象；在函数调用的时候，实参传递的是对象的引用
#2、了解原理后，就可以更好的去把控在函数内部处理是否会影响到函数外部的数据变化
#3、参数传递是通过对象的引用来完成
#不可变类型只能进行值传递，可变类型可以进行地址传递，通过对象引用完成

#python中使用lambda关键字创建匿名函数
#语法：lambda 参数1、参数2、参数3：表达式
#匿名函数冒号后面的表达式有且只有一个，注意：是表达式，而不是语句
#匿名函数自带return,而这个return的结果就是表达式计算后的结果
def computer(x,y):
    ...
#对应的匿名函数
    #return x+y
    #pass
M=lambda x,y:x+y
#通过变量去调用匿名函数
print(M(23,12))
#print(computer(10,20))
re=lambda a,b,c:a*b*c
print(re(1,2,3))

age=29
print("可以参军" if age > 18 else "继续上学") #可以替换传统双分支的写法

test=lambda x,y:x if x>y else y  
print(test(12,2))

res=(lambda x,y : x if x>y else y)(13,12) #直接调用
print(res)

var=lambda x:(x**2)+890
print(var(10))
#缺点：lambda只能是单个表达式，不是一个代码块，lambda的设计就是为了满足简单函数的场景，仅仅能封装有限的逻辑，复杂逻辑处理不了，此时必须要用def来处理

#阶乘
def digui(n):
    if n==1:
        return 1
    else:
        return digui(n-1)*n
print(digui(5))
# re = int(input("请输入数字："))
# print('阶乘结果为：{}'.format(digui(re)))

import os
def findFile(file_Path):
    listRs=os.listdir(file_Path) # 得到该路径下的所有文件
    for fileItem in listRs:
        full_path=os.path.join(file_Path,fileItem) # 获取完整的文件路径
        if os.path.isdir(full_path): # 判断是否是文件夹
            findFile(full_path) # 如果是一个文件夹，再次去递归
        else:
            print(fileItem)
            pass
        pass
    else:
        return
    pass
findFile('D:\Python\pydemo')
#打印结果：demo1.py  demo2.py  demo3.py  demo4.py  demo5.py  demo6.py


#递归函数优缺点  优点：递归使代码看起来更加整洁，优雅；可以用递归将复杂的任务分解成更简单的子问题；使用递归比使用一些嵌套迭代更加容易
#缺点：递归逻辑很难调试，递归条件处理不好容易造成程序无法结束，直到达到最大递归错误；递归占用大量内存，耗费计算机资源
