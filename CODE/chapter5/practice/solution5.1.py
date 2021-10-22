s = input("请输入一个字符串：")
while True:
    subStr = input("请输入要统计的字符串：")
    if subStr == "end":
        break;
    i = 0
    count = 0
    while i < len(s):
        index = s.find(subStr, i)
        if index > -1:
            count += 1
            i = index + len(subStr)
        else:
            break;
    
    print("'{}'在'{}'中出现了{}次".format(subStr, s, count))
