# 初始化函数
def init(data):
    data["d"] = {}
    data["names"] = []
    data["products"] = []
# 从控制台采集数据，并转化为列表或字典的函数，flag为True采集列表，为False，采集Dict
# msg表示提示文本，为了方便，这里假设输入的数据以逗号分隔，也可以将分隔符通过函数参数传入
def inputListOrDict(flag,msg):
    print(msg)
    inputStr = input(":")
    list = inputStr.split(",")
    # 返回列表
    if flag:
        return list
    
    keys = []
    values = []
    result = {}
    for i in range(len(list)):
        # key
        if i % 2 == 0:
            keys.append(list[i])
        else:
            values.append(list[i])
    # 返回字典
    return dict(zip(keys,values))
# 输出字典中的数据
def outDict(data):
    for key in data.keys():
        print(key,":",data[key])
