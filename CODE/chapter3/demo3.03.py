from click._compat import raw_input
name = raw_input("请输入您的名字：")        #  从控制台输入名字
if name.startswith("B"):                #  if代码块
    print("名字以B开头")
elif name.startswith("F"):                #  elif代码块
    print("名字以F开头")
elif name.startswith("T"):                #  elif代码块
    print("名字以T开头")
else:                                    #  else代码块
    print("名字以其他字母开头")
