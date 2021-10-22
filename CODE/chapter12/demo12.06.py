set1 = set(range(10))
print(type(set1))
print(set1)
set2 = set('hello')  # 将重复的集合元素去掉
print(set2)
set3 = set(['Bill','John','Mike','John'])
print(set3)

a = set((1,2,3))
b = set([3,5,1,7])
print(a.union(b))
print(a | b)

print(a & b)
print(a.intersection(b))

c = set([2,3])
print(c.issubset(a))
print(a.issubset(c))

print(c.issuperset(a))
print(a.issuperset(c))

d = set([1,2,3])
print(a == d)

print(a.difference(b))
print(a - b)

print(a.symmetric_difference(b))
print(a ^ b)
print((a - b) | (b - a))

x = a.copy()
print(x is a)
x.add(30)
print(x)
print(a)

print(d)
print(1 in d)
print(10 in d)
