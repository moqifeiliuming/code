def fun1():
    raise Exception("fun1抛出的异常")
def fun2():
    fun1()
def fun3():
    fun2()
def fun4():
    fun3()
def fun5():
    fun4()

fun5()