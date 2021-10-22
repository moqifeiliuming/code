import re
m = re.search('^The', 'The end.')
print(m)
if m is not None:
    print(m.group())
m = re.search('^The', 'end. The')
print(m)
if m is not None:
    print(m.group())

m = re.search('The$', 'end. The')
print(m)
if m is not None:
    print(m.group())
m = re.search('The$', 'The end.')
print(m)
if m is not None:
    print(m.group())
    
m = re.search(r'\bthis', "What's this?")
print(m)
if m is not None:
    print(m.group())
m = re.search(r'\bthis', "What'sthis?")
print(m)
if m is not None:
    print(m.group())

m = re.search(r'\bthis\b', "What's this?")
print(m)
if m is not None:
    print(m.group())
m = re.search(r'\bthis\b', "What's thisa")
print(m)
if m is not None:
    print(m.group())