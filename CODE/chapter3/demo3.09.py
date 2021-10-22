import random
'''
x = 0
break_flag = False
while x < 10:
    x += 1
    if x == random.randint(1,20):
        break_flag = True
        print(x)
        break;
if not break_flag:
    print("没有中断while循环")
'''

x = 0
while x < 10:
    x += 1
    if x == random.randint(1,20):
        print(x)
        break;    
else:
    print("没有中断while循环")
    
numbers = [1,2,3,4,5,6]
for number in numbers:
    if number == random.randint(1,12):
        print(number)
        break;
else:
    print("正常退出循环")
    
