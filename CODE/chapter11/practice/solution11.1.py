import re
s1 = '^[bh][aiu]t$'
list = ['bat','Bit','But','hAt','hit','hut']
for value in list:
    print(re.match(s1, value,re.I))
    