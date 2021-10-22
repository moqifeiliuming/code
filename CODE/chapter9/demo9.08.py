def fun1():
    try:
        print("fun1 正常执行")
    finally:
        print("fun1 finally")
def fun2():
    try:
        raise Exception 
    except:
        print("fun2 抛出异常")
    finally:
        print("fun2 finally")
def fun3():
    try:
        return 20
    finally:
        print("fun3 finally")
def fun4():
    try:
        x = 1/0
    except ZeroDivisionError as e:
        print(e)
    finally:
        print("fun4 finally")
        try:        
            del x
        except Exception as e:
            print(e)


fun1()
fun2()
print(fun3())
fun4()