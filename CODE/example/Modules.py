# import bmi as m   #导入bmi模块并设置别名为m
# 在使用import语句导入模块时，每执行一条import语句都会创建一个新的命名空间(namespace),并且在该命名空间中执行与.py文件相关的所有语句，
# 在执行时，需在具体的变量、函数和类名前加上"模块名."前缀
# 如果不想再每次导入模块时都创建一个新的命名空间，而是将具体的定义导入到当前的命名空间中，可使用from....import语句
# 命名空间可以理解为记录对象名字和对象之间对应关系的空间，目前大部分是通过字典来实现的
# 使用通配符“*”导入全部定义后，可以执行print(dir())语句显示导入的定义内容

def girth(width,height):
    return (width + height) * 2
def area(width,height):
    return width * height
if __name__=='__main__':
    print(girth(23,48))
    print(area(23,43))

# 当使用import语句导入模块时，默认情况下，会按照以下顺序进行查找
# 在当前目录（即执行的Python脚本文件所在目录）下查找
# 到PYTHONPATH（环境变量）下的每个目录中查找
# 到Python的默认安装目录下查找
import sys
print(sys.path)
# 使用import语句导入模块时，模块名是区分字母大小写的
# 通过该方法添加的目录只在执行当前文件的窗口中有效，窗口关闭后即失效
# 创建.pth文件之后，需要重新打开要执行的导入模块的Python文件，否则新添加的目录不起作用
# 在每个模块的定义中都包括一个记录模块名称的变量__name__，程序可以检查该变量，以确定他们在哪个模块中执行。
# 如果一个模块不是被导入到其他程序中执行，那可能在解释器的顶级模块中执行。顶级模块的__name__变量的值为__main__
# 使用模块可以避免函数名和变量名重名引发的冲突。包是一个分层次的目录结构，将一组功能相近的模块组织在一个目录下，既可以起到规范代码
# 的作用，又能避免模块名重名引起的冲突。包即是”文件夹“，在该文件夹下必须存在一个名称为"__init__.py"的文件

# 假如有一个名称为settings的包，在该包下有一个名称为size的模块，模块中有两个变量width,height
# 通过“import+完整包名+模块名”形式加载指定模块    import settings.size
# 通过“from+完整包名+import+模块名”形式加载指定模块    from settings import size
# 通过“from+完整包名+模块名+import+定义名”形式加载指定模块  from settings.size import width,height

_width = 800
_height = 600
def change(w,h):
    global _width
    _width = w
    global _height
    _height = h
def getWidth():
    global _width
    return _width
def getHeight():
    global _height
    return _height
# setting.py文件进行执行

import random
print(random.randint(0,10))  #生成一个 0 ~ 10 (包括0和10)的随机整数
# range(0,10)  #生成一个 0~9 的随机整数

import random
if __name__=='__main__':
    checkcode=""
    for i in range(4):
        index = random.randrange(0,4)  # 生成0~3中的一个数
        if index != i and index + 1 != i:
            checkcode += chr(random.randint(97,122)) #生成a-z中的一个小写字母
        elif index + 1 == i:
            checkcode += chr(random.randint(65,90))  #生成A-Z中的一个小写字母
        else:
            checkcode += str(random.randint(1,9))    #生成1-9中的一个数字
    print("验证码：",checkcode)

# 第三方模块，在Python官方推出的 http://pypi.python.org/pypi 中能找到
# help('modules')    查看Python中有哪些模块
# pip list     查看已经安装的第三方模块
