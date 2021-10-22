fibs = [0,1]
for i in range(10):
    fibs.append(fibs[-2] + fibs[-1])
print(fibs)

n = int(input("请输入一个整数："))
for i in range(n - 2):
    fibs.append(fibs[-2] + fibs[-1])
print(fibs)


