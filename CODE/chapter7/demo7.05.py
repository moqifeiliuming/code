# 未使用函数抽象的代码
data = {}
data["d"] = {}
data["names"] = []
data["products"] = []
print("请输入字典数据，key和value之间用逗号分隔")
dictStr = input(":")
# 将d拆分成key和value的两个集合
list = dictStr.split(",")
keys = []
values = []
for i in range(len(list)):
    # key
    if i % 2 == 0:
        keys.append(list[i])
    else:
        values.append(list[i])
data["d"].update(dict(zip(keys,values)))

print("请输入姓名，多个姓名之间用逗号分隔")
nameStr = input(":")
names = nameStr.split(",")
data["names"].extend(names)


print("请输入产品，多个产品之间用逗号分隔")
productStr = input(":")
products = productStr.split(",")
data["products"].extend(products)


for key in data.keys():
    print(key,":",data[key])


