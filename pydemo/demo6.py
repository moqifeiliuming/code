tup=()
tup=(1,2,3)
print(tup)
#tup.append(1,2,3)   元组不能进行修改
print(type(tup))
li=list(tup)
li.append('强制转换成功')    #列表可以进行修改
print(type(li))
print(li)     #此时为列表
tup1=tuple(li)
print(tup1)   #转换成元组

dic=dict(name='小明',age=18)  #创建一个字典
# dic={'name':'小明','age':18}
print(type(dic))
print(dic)
 
li=[1,2,3,0]   #all() 对象的元素除了是0，空，FALSE外都算TRUE，类似于and操作
print(all(li))  #结果为False
#any() 对象的元素除了全是FALSE外，都算TRUE，类似于OR操作
print(any(li))  #结果为True

#sort:用于列表和sorted
#zip()函数：用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表
#如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用*操作符，将元组解压为列表
s1=['a','b','c']
s2=['你','我','他']
s3=['我','你','真','她']
print(list(zip(s1)))   #[('a',), ('b',), ('c',)]
zipList=zip(s1,s2)
print(list(zipList)) #[('a', '你'), ('b', '我'), ('c', '他')]
zipl=zip(s1,s3)
print(list(zipl)) #[('a', '我'), ('b', '你'), ('c', '真')] 按照最少的进行压缩

#enumerate  函数用于将一个可比遍历的数据对象，如列表，元组、字符串等组合为一个索引序列，同时列出数据和数据下标
listObj=['a','b','c']
for item in enumerate(listObj):
    print(item)
    pass
print()

dicObj={}
dicObj['name']='liuming'
dicObj['hobby']='singing'
dicObj['pro']='arm'
for item in enumerate(dicObj):
    print(item)

for index,item in enumerate(dicObj):
    print(item)

for key,value in dicObj.items():
    print(value)

#set# set:不支持索引和切片，是一个无序的且不重复的容器；类似于字典，但只有key,没有value
set1={1,2,3}
dict1={}
print(type(set1))
print(type(dict1))
#添加操作
set1.add("python")
print(set1)
set2={2,3,4}
#差集操作
res=set1.difference(set2)
print(res)
print(set1-set2)

a={1,2,3,4}
a.pop()
print(a)
print(a.discard(2))
print(a)

#求三组连续自然数的和：求出1到10,20到30，和35到45的三个和
def sumRange(m,n):
    return sum(range(m,n+1))
    pass

print(sumRange(1,10))
print(sumRange(20,30))
print(sumRange(35,45))


#100个和尚吃100个馒头，大和尚一人吃3个馒头，小和尚三人吃1个馒头，请问大小和尚各多少？
def PersonCount():
    for a in range(1,100):
        if a*3 + (100-a)*(1/3) == 100:
            return (a,100-a)
        pass
    pass
re=PersonCount()
print(re)
print('大和尚{}人，小和尚{}人'.format(re[0],re[1]))


#指定一个列表，列表里含有唯一一个只出现过一次的数字，写程序找出这个独一无二的数字
li=[1,3,4,3,3,5,2,4,2,5,2,7,3,50]
set1=set(li)   #不可重复，把重复多余的去掉了
for i in set1:
    li.remove(i) #此时li中把多余的剩下来了
    pass
print(li)
set2=set(li)  #set2中把多余的剩下来了,此时set1和set2差集就是独一无二的数
for i in set1:
    if i not in set2:
        print(i,end=' ')
        pass
    pass
pass
print()

set1 = set(li)
for i in set1:
    li.remove(i)
set2 = set(li)
for i in set1:
    if i not in set2:
        print(i,end=' ')
