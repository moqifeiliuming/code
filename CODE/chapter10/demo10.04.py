class FactorialDict:
    def __init__(self):
        self.numDict = {}
    def factorial(self,n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n -1)
    def __getitem__(self,key):
        print('__getitem__方法被调用,key={}'.format(key))
        if key in self.numDict:
            return self.factorial(self.numDict[key])
        else:
            return 0
    def __setitem__(self,key, value):
        print('__setitem__方法被调用,key={}'.format(key))
        self.numDict[key] = int(value)
    def __delitem__(self,key):
        print('__delitem__方法被调用,key={}'.format(key))
        del self.numDict[key]
    def __len__(self):
        print('__len__方法被调用')
        return len(self.numDict)

d = FactorialDict()
d['4!'] = 4
d['7!'] = 7
d['12!'] = '12'



print('4!', '=', d['4!'])
print('7!', '=',d['7!'])
print('12!', '=',d['12!'])
print('len','=',len(d))
del d['7!']
print('7!', '=',d['7!'])
print('len','=',len(d))
