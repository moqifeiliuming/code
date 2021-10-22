class Fibonacci:
    def __init__(self):
        self.a = 0
        self.b = 1
    def __next__(self):
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        if result > 300: raise StopIteration
        return result
    def __iter__(self):
        return self

def fibonacciGenerator(): 
    for f in Fibonacci():
        yield f

for f in fibonacciGenerator():
    print(f, end = ' ')
