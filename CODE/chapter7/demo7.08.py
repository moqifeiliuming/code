def addNumbers(*numbers):
    result = 0
    for number in numbers:
        result += number
    return result
print(addNumbers(1,2,3,4,5))
print("--------------")
def calculator(type, *numbers):
    result = 0
    if type == "add":
        for number in numbers:
            result += number
    elif type == "sub":
        result = numbers[0]
        for i in range(1, len(numbers)):
            result -= numbers[i]
    elif type == "mul":
        result = 1
        for number in numbers:
            result *= number
    else:
        result = numbers[0]
        for i in range(1, len(numbers)):
            result /= numbers[i]
    return result

print(calculator("add",1,2,3,4,5,6))
print(calculator("sub",1234,44,54,12,57))
print(calculator("mul",1,2,3,4,5,6,7))
print(calculator("div",100,2,5))
print("--------------")
def calculator1(type, *numbers, ratio):
    return calculator(type, *numbers) * ratio
    
print(calculator1("add",1,2,3,4,5,6,ratio = 3))
print(calculator1("sub",1234,44,54,12,57,ratio = 2))
print(calculator1("mul",1,2,3,4,5,6,7,ratio = 4))
print(calculator1("div",100,2,5,ratio = 4))
print("--------------")
def calculator2(type, *numbers, ratio = 4):
    return calculator(type, *numbers) * ratio
print(calculator2("add",1,2,3,4,5,6))