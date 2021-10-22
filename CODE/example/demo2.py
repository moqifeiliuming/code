# 重点：输出的四种表现形式
# print("您已购买"+trainnumber+"次列车"+"长春-北京"+time+"开，请"+people+"尽快换取纸质版车票")
# print("您已购买%s次列车 长春-北京 %s开，请%s尽快换取纸质车票。"%(trainnumber,time,people)) 此时为三个字符串，为%s,要是为数值，则为%d
# print("您已购买{}次列车 长春-北京 {}开，请{}尽快换取纸质车票。".format(trainnumber,time,people))
# print("您已购买",trainnumber,"次列车 长春-北京",time,"开，请",people,"尽快换取纸质车票。")

# TV_plays=sorted(TV_plays, key=lambda s: s[1], reverse=True)  key为要排序的内容，reverse=True表示为降序，默认为False升序
#而lambda的意思为：定义一数组s,其内容为s[1]，即为TV_plays[1]的属性，收视率大小

r = list(range(10,20,2))
print(r)
enumerate
team=["火箭","勇士","开拓者","雷霆","爵士","鹈鹕","马刺","森林狼"]
for index,item in enumerate(team):
    if index %2 == 0:
        print(item+"\t\t",end='')
    else:
        print(item+"\n")
phone=["摩托罗拉","诺基亚","三星","OPPO"]
print(len(phone))
phone.append("华为")
print(len(phone))
print(phone)
seq=[]
seq.extend(phone)  #将phone列表中的东西全部添加到seq列表中,列表和数组的下标以0开始的
print(seq)
print(phone)
score=[98,99,96,97]
total=sum(score)
print(total)
#sorted(iterable,key=None,reverse=False)  #sort()方法和内置sorted()函数的作用基本相同，不同点在于使用sort()方法时，会改变原列表的元素排列顺序，而使用sorted()函数时，会建立一个原列表的副本，该副本为排序后的列表。

price = [1200,1356,4353,6454]
sale=[int(x * 0.5) for x in price]
sale1=[x for x in price if x > 4000]
print(price)
print(sale1)
print(sale)

res = tuple(range(10,20,2))
print(tuple)
print(res)
#del res

uk=('蓝山','绿水')
print(uk)
uk=uk + ('金山','银山')
# uk[1]=('青山')  错误
print(uk)    #元组是不可变序列，不能对它的单个元素进行修改，但是可以对元组进行重新赋值，并且可以对元组进行连接组合（但都要是元组类型）

number = (i for i in range(3))  #使用通过元组推导器生成的生成器对象，可以直接通过for循环遍历或者直接使用__next__()方法进行遍历
print(number.__next__())
print(number.__next__())
print(number.__next__())
print(number)    #遍历后原生成器对象已经不存在
number = tuple(number)
print(number)

'''
#元组和列表的区别：
列表属于可变序列，它的元素可以随时修改或者删除；元组属于不可变序列，其中的元素不可以修改，除非整体替换
列表可以使用append()，extend(),insert(),remove()和pop()等方法实现添加和修改元素，而元组没有这几个方法，不支持修改
列表可以使用切片访问和修改列表中的元素。元组也支持切片，但是它只支持通过切片访问元组中的元素，不支持修改
元组比列表的访问和处理速度快，所以当只是需要对其中的元素进行访问，而不进行任何修改时，建议使用元组
列表不能作为字典的键，而元组可以
'''

'''
#字典与列表相似，也是可变序列，不过它是无序的可变序列，保存的内容是以“键-值”对的形式存放的
#通过键而不是通过索引来读取
#字典是任意对象的无序集合
#字典是可变的，并且可以任意嵌套
#字典中的键必须唯一
#字典中的键必须不可变
'''
#字典的创建方法
dictionary={}
dictionary=dict()
#dictionary=dict(zip(list1,list2)) #zip()函数用于将多个列表或元组对应位置的元素组合为元组

name=['qi','mo','fei']
sign=['1','2','3']
dictionary=dict(zip(name,sign)) #两个列表合并成一个字典
print(dictionary)
print(dictionary.get('qi'))  #通过指定的键，来获得相应的值，此时用的是元组

name=('qi','mo','fei')
sign=['1','2','3']
dictionary={name:sign}
print(dictionary)

name=('qi','mo','fei')
sign=(1,2,3)
dictionary=dict(zip(name,sign))  #两个元组合并成一个字典
print(dictionary)

name=['1','2','3']
sign=['一','二','三']
name_sign=dict(zip(name,sign))
sign_all=['一','二','三']
nature=['1.0','2.0','3.0']
sign_dict=dict(zip(sign_all,nature))
print("3的标志是",name_sign.get("3"))
print("3的自然特点是",sign_dict.get(name_sign.get("3"))) #两个字典，从两个字典中取出相应的信息组合出想要的内容

dictionary.items()  #使用字典对象的items()方法可以获取字典的”键——值对"列表;字典对象中还提供了values()方法和keys()方法，用于返回字典的“值”和“键”列表，使用方法和items()类似
dictionary={'qq':123,'weixin':3243234,'feishu':23435}
for key,value in dictionary.items():
    print(key,"的信息是",value)

dictionary=dict((('1',1.0),('2',2.0),('3',3.0)))  #此时要多个小括号
dictionary['4']=4.0
print(dictionary)

import random
randomdict={i:random.randint(10,100) for i in range(1,5)}  #使用字典推导式可以快速生成一个字典，它的表现形式和列表推导类似。
print("生成的字典为：",randomdict)

name=['1','2','3']
sign=('你好','爱了','慕了')
# sign=(1,2,3)
dictionary={i:j +'呀' for i,j in zip(name,sign)} #注意与'呀'的对象形式一致
print(dictionary)

#集合
#直接使用{}创建集合，集合是可变序列，&,|,- 分别为交集、并集、差集运算符号
setname={1,2,3,4,5,6}
print(setname)
#使用set()函数进行创建集合
set1 = set("您好，世界，世界，您好")  #如果出现了重复元素的话，只会保留一个
set2 = set(('人生苦短','我用python'))
set1.add("我来了")  #集合是可变序列，通过add(),pop(),remove()方法进行操作
print(set1)
print(set2)

set1=set(['1','2','3','4'])
set2=set(['2','4','6','8'])
print('交集运算：',set1 & set2) #set1,set2共有的元素
print('并集运算：',set1 | set2) #set1，set2加起来的元素
print('差集运算：',set1 - set2)  #存在set1中，但set2中没有的元素

'''
数据结构            是否可变        是否重复     是否有序      定义符号
列表(list)           可变          可重复       有序          []
元组(tuple)          不可变        可重复       有序          ()
字典(dictionary)     可变          可重复       无序          {key:value}
集合(set)            可变          不可重复      无序         {}
'''
