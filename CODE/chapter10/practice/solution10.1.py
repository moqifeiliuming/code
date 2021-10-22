#  可无限迭代阶乘
class Factorial:
    def __init__(self):
        self.result = 1
        self.n = 0
    def __next__(self):
        if self.n == 0 or self.n == 1:
            self.n += 1
            self.result = 1
        else:
            self.result = self.result * (self.n)
            self.n += 1
        return self.result
    def __iter__(self):
        return self
    def reset(self):
        self.result = 1
        self.n = 0

factorial = Factorial()
for f in factorial:
    print(f, end = ' ')
    if f > 10000:
        break;

print()
it = iter(factorial)
print(next(it))
factorial.reset()
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))