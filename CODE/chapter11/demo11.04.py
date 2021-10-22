import re

s = '.ind'
m = re.match(s, 'bind')
if m is not None:
    print(m.group())
m = re.match(s,'binding')
print("<" + str(m))
m = re.match(s,'bin')
print(m)

m = re.search(s,'<bind>')
print(m.group())
print(m)

s1 = '3.14'
s2 = '3\.14'
m = re.match(s1, '3.14')
print(m)
m = re.match(s1, '3314')
print(m)

m = re.match(s2, '3.14')
print(m)
m = re.match(s2, '3314')
print(m)

