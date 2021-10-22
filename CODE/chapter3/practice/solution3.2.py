while True:
    x = input("请输入一个数：")
    if x == "end":
        break;
    num = int(x)
    if num % 2 == 0:
        print(x + "是偶数") 
    else:
        print(x + "是奇数")