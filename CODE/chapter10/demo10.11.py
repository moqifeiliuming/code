# 将迭代器转换为列表
class Fibonacci:
    def __init__(self):
        self.a = 0
        self.b = 1
    def __next__(self):
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        if result > 500: raise StopIteration
        return result
    def __iter__(self):
        return self

fibs1 = Fibonacci()
print(list(fibs1))
fibs2 = Fibonacci()
for fib in fibs2:
    print(fib, end = ' ')

