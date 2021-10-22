# try...except语句
# 在使用 try...except 语句捕获异常时，如果在except后面不指定异常名称，则表示捕获全部异常
# 使用 try...except 语句捕获异常后，当程序出错时，输出错误信息后，程序会继续执行
# 在except语句后面使用一对小括号将可能出现的异常名称括起来，多个异常名称之间使用逗号分隔
# 如果要想显示具体的出错原因，再加上as指定一个别名
def division():
    print('='*15,"分苹果了",'='*15)
    apple = int(input("请输入苹果的个数："))
    children = int(input("请输入小朋友的个数："))
    result = apple // children
    remain = apple - result * children
    if remain > 0:
        print(apple,"个苹果，平均分给了",children,"个小朋友，每人分",result,"个，剩下",remain,"个。")
    else:
        print(apple,"个苹果，平均分给了",children,"个小朋友，每人分",result,"个")

if __name__=='__main__':
    try:
        division()
    except ZeroDivisionError:
        print("\n出错了，苹果不能被0个小朋友分")
    except Value as e:
        print("输入错误：",e)
    else:
        print("苹果被顺利分完")
    finally:
        print("进行了一次分苹果的操作")

# 完整的异常处理语句应该包含finally代码块，无论程序中有无异常产生，finally代码块中的代码都会被执行
# 异常处理语句：try...except、try...except...else 和 try...except...finally
# ExceptionName[(reason)]为可选参数，用于指定抛出的异常名称以及异常信息的相关描述。如果省略，就会把当前的错误原样抛出

def division():
    print('='*15,"分苹果了",'='*15)
    apple = int(input("请输入苹果的个数："))
    children = int(input("请输入小朋友的个数："))
    result = apple // children
    remain = apple - result * children
    if apple < children:
        raise ValueError("苹果太少了，不够分")
    if remain > 0:
        print(apple,"个苹果，平均分给了",children,"个小朋友，每人分",result,"个，剩下",remain,"个。")
    else:
        print(apple,"个苹果，平均分给了",children,"个小朋友，每人分",result,"个")
if __name__=='__main__':
    try:
        division()
    except ZeroDivisionError:
        print("\n出错了，苹果不能被0个小朋友分")
    except ValueError as e:
        print("\n出错了~_~",e)
