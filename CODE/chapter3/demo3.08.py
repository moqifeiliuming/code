x = 0
while x < 100:
    if x == 5:
        break;
    print(x, end=" ") 
    x += 1
names = ["Bill", "Mike", "Mary"]
print("\nbreak语句在for循环中的应用")
for name in names:
    if not name.startswith("B"):
        break;
    print(name)

print("break语句在for循环中的应用")
for name in names:
    if name.startswith("B"):
        continue;
    print(name, end=" ")

print("\n嵌套循环")
arr1 = [1,2,3,4,5]
arr2 = ["Bill", "Mary", "John"]
arr = [arr1, arr2]
i = 0;
while i < len(arr):
    for value in arr[i]:
        print(value, end = " ")
    i += 1
    print()
        