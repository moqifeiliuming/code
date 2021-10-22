import os

# 获取系统信息
# 返回当前的工作目录
print('当前工作目录：',os.getcwd())
# 返回path指定的文件夹包含的文件或文件夹的名字的列表。
print('工作目录中包含的文件或文件夹的名字的列表')
print(os.listdir(os.getcwd()))
# 改变当前工作目录
os.chdir('../')
print('改变后的工作目录',os.getcwd())
print('新的工作目录中包含的文件或文件夹的名字的列表')
print(os.listdir(os.getcwd()))
