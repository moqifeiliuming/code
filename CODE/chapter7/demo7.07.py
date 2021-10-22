def sub1(m, n):
    return m - n

print(sub1(20,4))
print(sub1(4,20))

print(sub1(m = 20, n = 4))
print(sub1(n = 4, m = 20))

def sub2(m = 100, n = 50):
    return m - n

    
print(sub2())
print(sub2(45,21))
print(sub2(53, n = 12))
print(sub2(n = 123))
print(sub2(m = 542,n = 143))
print(sub2(53, m = 12))  