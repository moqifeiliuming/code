line = input("请输入行数（必须是奇数）：")
line = int(line)    # line表示菱形的总行数
if line % 2 != 0:
    f = open('stars.txt', 'w')
    import os
    spaceNum = line // 2        # spaceNum每行的最大空格数
    i = 1;
    lineSpaceNum = spaceNum     # lineSpaceNum表示当前行的前后空格数
    #  生成上三角形
    while lineSpaceNum >= 0:
        f.write(" " * lineSpaceNum)
        f.write("*" * (2 * i - 1))
        f.write(" " * lineSpaceNum + os.linesep)
        lineSpaceNum -= 1
        i += 1
    i -= 2
    lineSpaceNum+=2
    #  生成下三角形
    while lineSpaceNum <= spaceNum:

        f.write(" " * lineSpaceNum)
        f.write("*" * (2 * i - 1) )
        f.write(" " * lineSpaceNum + os.linesep)
        lineSpaceNum += 1
        i -= 1
    f.close()
else:
    print("必须输入奇数")