import re
s = '^\d{4}\s+\d{4}\s+\d{4}\s+\d{4}$'
list = ['1234 5432 1532 5432','12346 743 1335 8765','1234543212347654']
for value in list:
    print(re.match(s, value,re.I))
    
