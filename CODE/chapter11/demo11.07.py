import re
m = re.match('(\d{3})-(\d{4})-([a-z]{2})', '123-4567-xy')

if m is not None:
    print(m.group())
    print(m.group(1))
    print(m.group(2))
    print(m.group(3))
    print(m.groups())
print('-----------------')
m = re.match('(\d{3}-\d{4})-([a-z]{2})', '123-4567-xy')
if m is not None:
    print(m.group())
    print(m.group(1))
    print(m.group(2))
    print(m.groups())
print('-----------------')
m = re.match('\d{3}-\d{4}-([a-z]{2})', '123-4567-xy')
if m is not None:
    print(m.group())
    print(m.group(1))
    print(m.groups())
print('-----------------')
m = re.match('\d{3}-\d{4}-[a-z]{2}', '123-4567-xy')
if m is not None:
    print(m.group())
    print(m.groups())