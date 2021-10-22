numStr= input('请输入一个大于1的整数：')
n = int(numStr)
m = n * n
i = 1
numbers = []
values = []
# 通过循环产生二维列表
while i <= m:
    values.append(i)
    if i % n == 0:
        numbers.append(values.copy())
        values.clear()
    i += 1
print(numbers)
i = 0;
j = 1;
#  通过二重循环交互相应元素的值
while i < n:
    while j < n:
        numbers[i][j],numbers[j][i] =numbers[j][i],numbers[i][j]
        j+=1 
    i+=1
print(numbers)