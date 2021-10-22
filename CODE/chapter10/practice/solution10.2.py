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
        if self.result > 100000: raise StopIteration
        return self.result
    def __iter__(self):
        return self
    def reset(self):
        self.result = 1
        self.n = 0

factorial = Factorial()
print(list(factorial))   # 转换为序列