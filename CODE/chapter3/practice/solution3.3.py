line = input("请输入行数（必须是奇数）：")
line = int(line)    # line表示菱形的总行数
if line % 2 != 0:
    spaceNum = line // 2        # spaceNum每行的最大空格数
    i = 1;
    lineSpaceNum = spaceNum     # lineSpaceNum表示当前行的前后空格数
    #  生成上三角形
    while lineSpaceNum >= 0:
        print(" " * lineSpaceNum, end="")
        print("*" * (2 * i - 1),end="")
        print(" " * lineSpaceNum)
        lineSpaceNum -= 1
        i += 1
    i -= 2
    lineSpaceNum+=2
    #  生成下三角形
    while lineSpaceNum <= spaceNum:

        print(" " * lineSpaceNum, end="")
        print("*" * (2 * i - 1),end="")
        print(" " * lineSpaceNum)
        lineSpaceNum += 1
        i -= 1
else:
    print("必须输入奇数")