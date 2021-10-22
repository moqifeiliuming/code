list = ['a','b','c','d','e']
s = "+"
print(s.join(list))

dirs = '','usr','local','nginx',''
linuxPath = '/'.join(dirs)
windowPath = 'C:' + '\\'.join(dirs)
print(linuxPath)
print(windowPath)

numList = [1,2,3,4,5]
print(s.join(numList)) 
