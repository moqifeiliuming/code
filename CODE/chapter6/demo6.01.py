'''
names = ["Bill", "Mike", "John", "Mary"]
numbers = ["1234", "4321", "6645", "7753"]

print(numbers[names.index("Mike")])
print(names[numbers.index("6645")])

phoneBook = {"Bill":"1234", "Bill1":"4321", "John":"6645","Mary":"7753"}
print(phoneBook["Bill"])

items = [["Bill","1234"], ("Mike","4321"),["Mary", "7753"]]

d= dict(items)
print(d)

items = dict(name = "Bill", number = "5678", age = 45)
print(items)
#items = dict([names, numbers])
#print([names, numbers])
'''

items = []
while True:
    key = input("请输入Key：")
    if key == "end":
        break;
    value = input("请输入value：")
    keyValue = [key, value]
    items.append(keyValue)

d = dict(items)
print(d)
    