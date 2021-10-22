#raise Exception
#raise Exception("这是自己主动抛出的一个异常")
#raise ArithmeticError
# raise ArithmeticError("这是一个和数值有关的异常")
from boto.codedeploy.exceptions import InvalidRoleException
raise InvalidRoleException(2,"这是一个和Role有关的异常")

