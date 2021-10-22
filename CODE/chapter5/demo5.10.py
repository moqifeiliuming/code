s = input("请输入一个大字符串：")

while True:
    subString = input("请输入一个子字符串：")
    if subString == "end":
        break 
    startStr = input("请输入开始索引：")
    endStr = input("请输入结束索引：")
    start = 0
    end = len(s)
      
    if startStr != "":
        start = int(startStr)
    if endStr != "":
        end = int(endStr)
    print("'{}'在'{}'的出现的位置是{}：".format(subString, s,s.find(subString,start,end)))