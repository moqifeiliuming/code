import fileinput
fileobj = fileinput.input('./files/urls.txt')

print(type(fileobj))
print(fileobj.readline().rstrip())
for line in fileobj:    
    line = line.rstrip()
    if line != '':
        print(fileobj.lineno(),':',line)
    else:
        print(fileobj.filename())  # 必须在第1行读取后再调用，否则返回None