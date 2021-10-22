dict = {"name":"Bill", "age":34, "sex":"男", "salary":"3456"}

# 遍历key
for key in dict:
    print(key, "=", dict[key], end = " ")

print()
# 遍历key和value
for key,value in dict.items():
    print(key, "=", value, end = " ")
print();
# 并行迭代
list1 = [1,2,3,4,5]
list2 = ["a", "b", "c", "d", "e"]
for i  in range(len(list1)):
    print("list1[" + str(i) + "]", "=", list1[i], "list2[" +str(i) + "]" ,"=", list2[i],end=" ")
    
print();
# 压缩
for value in zip(list1, list2):
     print(value, end = " ")
print()
list3 = ['x', 'y']
for value in zip(list2, list3):
    print(value, end = " ")
    
#  反转排序迭代
print()
values1 = [4,1,3,6,5,2,8]
print(sorted(values1))

values2 = reversed(values1)
for v in values2:
    print(v, end=" ")
print()

print(''.join(list(reversed("hello world"))))


