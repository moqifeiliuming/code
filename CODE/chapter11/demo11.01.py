import re
m = re.match('hello', 'hello')
if m is not None:
    print(m.group())
print(m.__class__.__name__)

m = re.match('hello', 'world')
if m is not None:
    print(m.group())
print(m)
# 只要模式从字符串起始位置开始，也可以匹配成功
m = re.match('hello', 'hello world')
if m is not None:
    print(m.group())
print(m)