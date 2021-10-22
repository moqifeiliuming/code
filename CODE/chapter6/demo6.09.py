dict = {"help":"帮助", "bike":"自行车", "geek":"极客","China":"中国"}
print(dict.items())
for key_value in dict.items():
    print("key","=",key_value[0],"value","=",key_value[1])
print(("bike","自行车") in dict.items())

dict_items = dict.items()
dict["bike"] = "自行车； 摩托车； 电动自行车；"
print(dict_items)

print(dict.keys())
for key in dict.keys():
    print(key)