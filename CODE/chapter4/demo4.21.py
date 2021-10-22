spaceNum = 5
i = 1
lineSpaceNum =spaceNum   # 表示当前行的前后空格数
triangle = []            # 二维列表
# 开始生产三角形
while lineSpaceNum >= 0:
    # 生成星号左侧空格列表
    leftSpaceList = [' '] * lineSpaceNum
    # 生成星号列表
    starList = ['*'] * (2 * i - 1)
    # 生成星号右侧空格列表
    rightSpaceList = [' '] * lineSpaceNum
    # 生成每一行的列表
    lineList = leftSpaceList + starList + rightSpaceList
    triangle.append(lineList)
    lineSpaceNum -= 1
    i += 1
for line in triangle:
    print(line)
