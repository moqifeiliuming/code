while True:
    expression= input("请输入表达式：")
    if expression == "end":
        break;
    print("计算结果：",eval(expression))
