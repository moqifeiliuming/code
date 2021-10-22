import re
s = 'Bill|Mike|John'
m = re.match(s, 'Bill')
if m is not None:
    print(m.group())
m = re.match(s, "Bill:my friend")
if m is not None:
    print(m.group())

m = re.search(s,'Where is Mike?')
if m is not None:
    print(m.group())
print(m)
