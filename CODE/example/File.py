# 文件mode参数的参数值说明
# r    以只读模式打开文件，文件的指针将会放在文件的开头
# rb   以二进制格式打开文件，并且采用只读模式。文件的指针将会放在文件的开头，一般用于非文本文件，如图片、声音等
# r+   打开文件后，可以读取文件内容，也可以写入新的内容覆盖原有内容（从文件开头进行覆盖）
# rb+  以二进制格式打开文件，并且采用读写模式。文件的指针将会放在文件的开头。一般用于非文本文件，如图片、声音等
# w    以只写模式打开文件
# wb   以二进制格式打开文件，并且采用只写模式。一般用于非文本文件，如图片、声音等
# w+   打开文件后，先清空原有内容，使其变成一个空的文件，对这个空文件有读写权限
# wb+  以二进制格式打开文件，并且采用读写模式。一般用于非文本文件，如图片、声音等
# a    以追加模式打开一个文件。如果该文件已经存在，文件指针将放在文件的末尾（即新内容会被写入到已有内容之后），否则，创建新文件用于写入
# ab   以二进制格式打开文件，并且采用追加模式。如果该文件已经存在，文件指针将放在文件的末尾（即新内容会被写入到已有内容之后），否则，创建新文件用于写入
# a+   以读写模式打开文件。如果该文件已经存在，文件指针将放在文件的末尾（即新内容会被写到已有内容之后），否则，创建新文件用于读写
# ab+  以二进制格式打开文件，并且采用追加模式。如果该文件已经存在，文件指针将放在文件的末尾（即新内容会被写入到已有内容之后），否则，创建新文件用于读写

print("\n","="*10,"蚂蚁庄园动态","="*10)
file = open('message.txt','w')
print("\n 即将显示.....\n")

file = open('picture.png','rb')
print(file)
file.close()

print("\n","="*10,"蚂蚁庄园动态","="*10)
with open('message.txt','w') as file:
    pass
print("\n 即将显示....\n")

print("\n","="*10,"蚂蚁庄园动态","="*10)
file = open('message.txt','w')  # 创建或打开保存蚂蚁庄园动态信息的文件
# 写入一条动态信息
file.write("你使用了一张加速卡，小鸡撸起袖子开始双手吃饲料，进食速度大大加快。\n")
print("\n 写入了一条动态.....\n")
file.close()

print("\n","="*10,"蚂蚁庄园动态","="*10)
file = open('message.txt','a')  # 创建或打开保存蚂蚁庄园动态信息的文件
# 追加一条动态信息
file.write("mingri的小鸡在你的庄园待了22分钟，吃了6g饲料之后，被你赶走了。\n")
print("\n 追加了一条动态.....\n")
file.close()

# 在Python的文件对象中除了提供write()方法，还提供了writelines()方法，可以实现把字符串列表写入文件，但是不添加换行符
with open('message.txt','r') as file:
    string = file.read(9)
    print(string)  # 读取前9个字符

# with open('message.txt','r') as file:
#     file.seek(19)
#     string = file.read(13)
#     print(string)
# 在使用seek()方法时，如果采用GBK编码，那么offset的值时按一个汉字(包括中文标点符号)占两个字符计算，而采用UTF-8编码，则一个汉字占3个字符。

print("\n","="*25,"蚂蚁庄园动态","="*25,'\n')
with open('message.txt','r') as file:
    message = file.read()
    print(message)
    print("="*25,"蚂蚁庄园动态","="*25)

# file.readline()   # 读取一行
print("\n","="*35,"蚂蚁庄园动态","="*35,'\n')
with open('message.txt','r') as file:
    number = 0
    while True:
        number += 1
        line = file.readline()
        if line == '':
            break
        print(number,line,end='\n')
print("="*39,"over","="*39,"\n")

# file.readlines()  # 读取全部行
print("\n","="*25,"蚂蚁庄园动态","="*25,'\n')
with open('message.txt','r') as file:
    message = file.readlines()
    print(message)
print("\n","="*25,"蚂蚁庄园动态","="*25,'\n')

# 逐行输出，且输出了全部的内容
print("\n","="*25,"蚂蚁庄园动态","="*25,'\n')
with open('message.txt','r') as file:
    messageall = file.readlines()
    for message in messageall:
        print(message)
print("="*25,"蚂蚁庄园动态","="*25,'\n')

import os
import os.path
os.name
print(os.name)
# nt为 Windows操作系统，posix为 Linux，Unix或Mac OS操作系统
# linesep: 用于获取当前操作系统上的换行符
# sep: 用于获取当前操作系统所使用的路径分隔符

# 相对路径：当前工作目录是指当前文件所在的目录，用os模块提供的getcwd()函数获取当前工作目录
# 在Python中，指定文件路径时需要对路径分隔符"\"进行转义，即将路径中的"\"替换为"\\"。
# 在指定文件路径时，也可以在表示路径的字符串前面加上字母r(或R)，那么该字符串将原样输出，该路径中的分隔符就不需要进行转义了
# with open(r"demo\message.txt") as file:
#     pass

# 绝对路径：是指在使用文件时指定文件的实际路径，不依赖于当前工作目录。可以通过os.path模块提供的abspath()函数获取一个文件的绝对路径
# os.path.abspath(path)  # path为要获取绝对路径的相对路径

# 创建目录
# 创建一级目录，可以通过os模块提供的mkdir()函数实现，该函数只能创建指定路径中的最后一级目录，如果该目录的上一级不存在，则抛出FileNotFoundError异常
import os
path = "C:\\demo1"
if not os.path.exists(path):
    os.mkdir(path)
    print("目录创建成功")
else:
    print("该目录已经存在！")
# 创建多级目录，可以使用os模块提供的makedirs()函数，该函数用于采用递归的方式创建目录
import os
os.makedirs("C:\\demo\\test\\dir\\mr")

# 删除目录可以通过使用os模块提供的rmdir()函数实现，通过rmdir()函数删除目录时，只有当要删除的目录为空时才起作用。
import os
path = "C:\\demo\\test\\dir\\mr"
if os.path.exists(path):
    os.rmdir("C:\\demo\\test\\dir\\mr")
    print("目录删除成功")
else:
    print("该目录不存在")
# 使用rmdir()函数只能删除空的目录，如果想要删除非空目录，则需要使用Python内置的标准模块shutil的rmtree()函数实现
import shutil
shutil.rmtree("C:\\demo\\test")

