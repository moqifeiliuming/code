name = input("你叫什么名字？")
if  name.startswith("Bill"):            #  以Bill开头的姓名
    if name.endswith("Gates"):            #  以Gates结尾的姓名
        print("欢迎Bill Gates先生")
    elif name.endswith("Clinton"):        #  以Clinton结尾的姓名
        print("欢迎克林顿先生")
    else:                                #  其他姓名
        print("未知姓名")
elif name.startswith("李"):                #  以“李”开头的姓名
    if name.endswith("宁"):                #  以“宁”结尾的姓名
        print("欢迎李宁老师")
    else:                                #  其他姓名
        print("未知姓名")
else:                                    #  其他姓名
    print("未知姓名")
