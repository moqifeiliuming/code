
class CounterList(list):
    def __init__(self,*args):
        super().__init__(*args)
        self.counter = 0
    def __getitem__(self,index):
        self.counter += 1
        return super(CounterList, self).__getitem__(index)
c = CounterList(range(10))
print(c)
c.reverse()
print(c)
del c[2:7]
print(c)
print(c.counter)
print(c[1] + c[2])
print(c.counter)

class CounterDict(dict):
    def __init__(self,*args):
        super().__init__(*args)
        self.counter = 0
    def __getitem__(self,key):
        self.counter += 1
        return super(CounterDict, self).__getitem__(key)
d = CounterDict({'name':'Bill'})
print(d['name'])
print(d.get('age'))    
d['age'] = 30
print(d['age'])
print(d.counter)


class MultiString(str):
    def __new__(cls, *args, sep = ' '):
        s = ''
        for arg in args:
            s += arg + sep
        index = -len(sep)
        if index == 0:
            index = len(s)
        return str.__new__(cls, s[:index])
    def __init__(self, *args, sep = ' '):
        pass
cs1 = MultiString('a', 'b', 'c')

cs2 = MultiString('a', 'b', 'c', sep=',')
cs3 = MultiString('a', 'b', 'c', sep='')
print('[' + cs1 + ']')
print('[' + cs2 + ']')
print('[' + cs3 + ']')

