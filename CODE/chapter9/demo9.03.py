x = None

while True:
    try:
        if x == None:
            x = int(input("请输入分子："))
        y = int(input("请输入分母："))
        print("x / y = {}".format(x / y))
        break;
    except :
        print("分母不能为0，请重新输入分母！")


