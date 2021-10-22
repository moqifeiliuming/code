def test(flag):
    print("这是在函数中打印的信息")
    if flag:
        return 
    print("这行信息只有在flag为False是才会输出")

test(False)
print("----------")
returnValue = test(True)

print(returnValue)