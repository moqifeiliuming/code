a = set([1,2])
b = set([10,20])

a.add(4)
print(a)
# a.add(b)
a.add(frozenset(b))
print(a)
d = {'Bill':30,'Mike':40}
#d[a] = 60
d[frozenset(a)] = 60

print(d)
t = [1,2,3]
tt = (1,2,3)
# d[t] = 111
#a.add(t)
#a.add(d)
a.add(tt)
print(a)



