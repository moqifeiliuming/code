# 引用string模块中的Template类
from string import Template
template1 = Template("$s是我最喜欢的编程语言, $s非常容易学习，而且功能强大")
# 指定格式化参数s的值是Python
print(template1.substitute(s='Python'))
# 当格式化参数是一个字符串的一部分时，为了和字符串的其他部分区分开，
# 需要用一对大括号将格式化参数变量括起来
template2 = Template("${s}stitute")
print(template2.substitute(s='sub'))

template3 = Template("$dollar$$相当于多少$pounds")
# 替换两个格式化参数变量
print(template3.substitute(dollar=20,pounds='英磅'))

template4 = Template("$dollar$$相当于多少$pounds")
data = {}
data['dollar'] = 100
data['pounds'] = '英磅'
# 使用字典指定格式化参数值
print(template4.substitute(data))
