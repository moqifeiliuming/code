class RightTriangle:
    def __init__(self):
        self.n = 1
    def __next__(self):        
        result = '*' * (2 * self.n - 1)
        self.n += 1
        return result
    def __iter__(self):
        return self
rt = RightTriangle()
for e in rt:
    if len(e) > 20:
        break;
    print(e)
class Fibonacci:
    def __init__(self):
        self.a = 0
        self.b = 1
    def __next__(self):
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result
    def __iter__(self):
        return self

fibs = Fibonacci()
for fib in fibs:
    print(fib, end = " ")
    if fib > 500:
        break;

