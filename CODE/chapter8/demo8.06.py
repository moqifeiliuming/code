class Calculator:
    def calculate(self,expression):
        self.value = eval(expression)
    def printResult(self):
        print("result:{}".format(self.value))

    
class MyPrint:
    def printResult(self):
        print("计算结果：{}".format(self.value))
    def aa(self,a):
        return 30
class NewCalculator(Calculator, MyPrint):
    pass
class NewCalculator1(MyPrint,Calculator):
    pass
calc = NewCalculator()
calc.calculate("1 + 3 * 5")
calc.printResult()
print(NewCalculator.__bases__)

calc1 = NewCalculator1()
print(NewCalculator1.__bases__)
calc1.calculate("1 + 3 * 5")
calc1.printResult()


