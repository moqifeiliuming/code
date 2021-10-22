class CustomException1(Exception):
    pass
class CustomException2(Exception):
    pass
class CustomException3(Exception):
    pass
import random


def raiseException():
    n = random.randint(1,3)
    print("抛出CustomException{}异常".format(n))
    if n == 1:
        raise CustomException1
    elif n == 2:
        raise CustomException2
    else:
        raise CustomException3
try:
    raiseException()
except (CustomException1,CustomException2,CustomException3):
    print("******执行异常处理程序******") 