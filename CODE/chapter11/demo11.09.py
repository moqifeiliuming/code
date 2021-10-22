import re
s = '12-a-abc54-a-xyz---78-A-ytr'

result = re.findall(r'\d\d-a-[a-z]{3}',s)
print(result)

result = re.findall(r'(\d\d)-a-([a-z]{3})',s)
print(result)

result = re.findall(r'\d\d-a-[a-z]{3}',s,re.I)
print(result)

result = re.findall(r'(\d\d)-a-([a-z]{3})',s,re.I)
print(result)

it = re.finditer(r'(\d\d)-a-([a-z]{3})',s,re.I)
for result in it:
    print(result.group(),end=' < ')
    groups = result.groups()
    for i in groups:
        print(i,end = ' ')
    print('>')
