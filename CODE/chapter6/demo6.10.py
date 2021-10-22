dict = {'c':10,'a':40,'b':12,'x':44}
dict['1'] = 3
dict['5'] = 3
print(dict.pop('b'))
for i in range(len(dict)):
    print(dict.popitem())
