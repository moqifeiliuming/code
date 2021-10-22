import re
result = re.split(';','Bill;Mike;John')
print(result)
result = re.split('[,;.\s]+','a,b,,d,d;x    c;d.  e')
print(result)
result = re.split('[a-z]{3}-[0-9]{2}','testabc-4312productxyz-43abill')
print(result)

result = re.split('[a-z]{3}-[0-9]{2}','testabc-4312productxyz-43abill',maxsplit=1)
print(result)