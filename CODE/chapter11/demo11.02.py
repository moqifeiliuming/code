import re

m = re.match('python','I love python.')
if m is not None: 
    print(m.group())
print(m)

m = re.search('python','I love python.')
if m is not None: 
    print(m.group())
print(m)


