print(1,end=" ")
print(2,end=" ")
print(3,end=" ")
print(4,end=" ")
print(5,end=" ")
print(6,end=" ")
print(7,end=" ")
print(8,end=" ")
print(9,end=" ")
print(10)

# 用while循环输出1到10
print("用while循环输出1到10")
x = 1
while x <= 10:
    print(x,end=" ")
    x += 1

#  定义一个数组
numbers = [1,2,3,4,5,6,7,8,9,10]
print("\n用for循环输出数组中的值（1到10）")
for num in numbers:
    print(num, end= " ")
    
numbers = range(1,10000)
print("\n用for循环输出数组中的值（1到9999）")
for num in numbers:
    print(num, end= " ")
print("\n用for循环输出数组中的值的乘积（0到99）")
for num in range(100):
    print(num * num, end= " ")