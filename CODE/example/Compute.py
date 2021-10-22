import Modules   # 此处如果写成print(girth(23,48)就会报错，没有找到girth,area
# 在使用import语句导入模块时，每执行一条import语句都会创建一个新的命名空间(namespace),并且在该命名空间中执行与.py文件相关的所有语句，
# 在执行时，需在具体的变量、函数和类名前加上"模块名."前缀
if __name__=='__main__':
    print(Modules.girth(23, 48))
    print(Modules.area(23, 43))

# 如果不想再每次导入模块时都创建一个新的命名空间，而是将具体的定义导入到当前的命名空间中，可使用from....import语句
from Modules import girth
from Modules import *
from Modules import area
if __name__=='__main__':
    print(girth(23, 48))
    print(area(23, 43))
