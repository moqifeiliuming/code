import re
m = re.match('[ab][cd][ef][gh]', 'adfh')
print(m.group())

m = re.match('[ab][cd][ef][gh]', 'bceg')
print(m.group())

m = re.match('[ab][cd][ef][gh]', 'abceh')  # 不匹配
print(m)

m = re.match('ab[cd][ef][gh]', 'abceh')  # 匹配
print(m.group())
print(m)

m = re.match('abcd|efgh', 'efgh')  # 匹配
print(m.group())
print(m)


