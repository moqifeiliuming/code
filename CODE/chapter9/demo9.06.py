class NegativeException(Exception):
    pass
class ZeroException(Exception):
    pass

class SpecialCalc:
    def add(self,x,y):
        if x < 0 or y < 0:
            raise NegativeException("x和y都不能小于0")
        return x + y
    def sub(self,x,y):
        if x - y < 0:
            raise NegativeException("x与y的差值不能小于0")
        return x - y
    def mul(self,x,y):
        if x == 0 or y == 0:
            raise ZeroException("x和y都不能等于0")
        return x * y
    def div(self,x,y):
        return x / y

while True:
    try:
        calc = SpecialCalc()
        expr = input("请输入要计算的表达式，例如，add(1,2)：")
        if expr == ":exit":
            break;
        result = eval('calc.' + expr)
        print("计算结果：{:.2f}".format(result))
    except (NegativeException,ZeroException) as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)    
    except:
        print("******其他异常******")
        