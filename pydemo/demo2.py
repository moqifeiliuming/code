row = 1
while row <= 7:
    j = 1
    while j <= row:
        print('*', end=' ')
        j += 1
        pass
    row += 1
    print()  # 换行符

row = 1
while row <= 5:
    j = 1
    while j <= 5 - row:
        print(' ', end=' ')
        j += 1
        pass
    k = 1
    while k <= 2 * row - 1:
        print('*', end=' ')
        k += 1
        pass
    print()  # 换行符
    row += 1

# row = 1
# while row <= 5:
#     i = 1
#     while i <= 5 - row:
#         print(' ',end=' ')
#         i+=1
#         pass
#     j = 1
#     while j <= 2 * row - 1:
#         print('*',end=' ')
#         j+=1
#         pass
#     row+=1
#     print()

tags = "我是一个中国人"
for item in tags:
    print(item, end=' ')
    pass

# for data in range(1,101):
#    print(data,end=' ')
#    pass

sum = 0
for data in range(1, 101):
    sum += data
    pass
print()
print("sum=%d" % sum)

# while使用：适用于对未知的循环次数
# for使用：适用于一直的循环次数【遍历】

for i in range(1, 10):
    for j in range(1, i + 1):  # 左闭右开的区间
        print("%d*%d=%2d" % (j, i, j * i), end=' ')
        pass
    print()
    pass

# for----else
for item in range(1, 11):
    print(item, end=' ')
    pass

print()
user = 'lm'
pwd = '123'
for i in range(3):
    u = input("请输入账号:")
    p = input("请输入密码:")
    if u == user and p == pwd:
        print("登录成功")
        break
        pass
    pass
else:
    print("您的账号已经被锁定")

print()
# while-----else
# index=1
# while index<=10:
#     print(index,end=' ')
#     index+=1
#     pass
# else:
#     print("else执行了么")
for index in range(1, 11):
    print(index, end=' ')
    pass
print()

# 小王BMI指数
height = 1.71
weight = 70.5
BMI = weight / (height ** 2)
if BMI < 18.5:
    print("小王体重过轻")
    pass
elif 18.5 <= BMI <= 25:
    print("标准体重")
    pass
elif 25 <= BMI <= 28:
    print("微胖")
    pass
elif 28 <= BMI <= 32:
    print("体重过胖")
    pass
else:
    print("严重肥胖")
    pass

#猜年龄游戏
import random
a=random.randint(1,100)
times=0
while times<=3:
    age=int(input('请输入您要猜的年龄：'))
    if age==a:
        print('恭喜猜对了')
        break
    elif age > a :
        print('猜大了')
    else:
        print('猜小了')
    times+=1
    if times==3:
        choose=input("想不想继续猜呢 Y/N?")
        if choose=='Y' or choose=='y':
            times=0
        elif choose=='N' or choose=='n':
            times=4
        else:
            print("请输入正确的标记")

import random
time = 0
digit = random.randint(0,101)
while time <= 3:
    age = int(input("请输入您要猜的数字："))
    if age == digit:
        print("您猜对了")
        break
    elif age < digit:
        print("您猜小了，请继续")
    else:
        print("您猜大了，请继续")
    if time == 3:
        choice = input("想不想继续玩呢，Y表示想，N表示不想Y/N：")
        if choice == 'Y' or choice == 'y':
            time = 0
        elif choice == 'N' or choice =='n':
            time = 4
        else:
            print("请输入正确的形式")
