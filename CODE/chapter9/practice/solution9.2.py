class JCException(Exception):
    pass
class JC:
    def compute(self, n):
        if n < 0:
            raise JCException('只能计算0或正整数的阶乘！')
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.compute(n - 1)
jc = JC()
print(jc.compute(10))
try:
    print(jc.compute(-10))
except JCException as e:
    print(e)
    