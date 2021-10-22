# 字典中的键可以是任意不可变的类型
dict = {}
dict[20] = "Bill"   
dict["Mike"] = {'age':30,'salary':3000}
dict[(12, "Mike", True)] = "hello"
print(dict)

#list = []
#list[30] = "hello"   # 抛出异常

#  演示key in dict操作

IDEs = {
    'eclipse':
        {
        'languages':['Java', 'Python', 'JavaScript','PHP'],
        'organization':'Eclipse基金会'
        },
    'visualstudio':
        {
        'languages':['C#','C++', 'VB.NET'],
        'organization':'微软'
        },
    'webstorm':
        {
        'languages':['JavaScript'],
        'organization':'JetBrains'
        }
    
    }

labels = {
    'languages':'支持的编程语言',
    'organization':'所属机构'
    }
IDE = input('请输入IDE的名字：')
findIDE = IDE.replace(" ", "").lower()
choice = input('要查询IDE支持的编程语言(lang)还是所属组织机构(org)？')
if choice == "lang": key = 'languages'
if choice == "org": key = 'organization'

if findIDE in IDEs:
    print("{}{}是{}.".format(IDE, labels[key], IDEs[findIDE][key]))

