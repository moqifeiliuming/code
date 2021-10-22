def fibs(n):
    result = [0,1]
    for i in range(n - 2):
        result.append(result[-2] + result[-1])
    return result

while True:
    value = input("请输入一个整数：")
    if value == ":exit":
        break;
    n = int(value)
    print(fibs(n))



