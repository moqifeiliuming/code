from dataman import *
data1 = {}
data2 = {}
init(data1)
init(data2)
data1["d"].update(inputListOrDict(False, "请输入字典数据，key和value之间用逗号分隔"))
data1["names"].extend(inputListOrDict(True, "请输入姓名，多个姓名之间用逗号分隔"))
data1["products"].extend(inputListOrDict(True, "请输入产品，多个产品之间用逗号分隔"))

data2["d"].update(inputListOrDict(False, "请输入字典数据，key和value之间用逗号分隔"))
data2["names"].extend(inputListOrDict(True, "请输入姓名，多个姓名之间用逗号分隔"))
data2["products"].extend(inputListOrDict(True, "请输入产品，多个产品之间用逗号分隔"))

outDict(data1)
outDict(data2)