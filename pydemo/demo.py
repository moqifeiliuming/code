score = 40
if score >= 60:
    print("成绩还行")
    pass
print("成绩不行")

score = int(input("请输入成绩："))
if score >= 90:
    print("成绩优异")
    pass
elif score >= 80:
    print("成绩良好")
    pass
elif score >= 70:
    print("成绩中等")
    pass
elif score >= 60:
    print("成绩及格")
    pass
else:
    print("不及格")
    pass

print("成绩运行结束")

import random
person=int(input("请出拳：[0:石头 1：剪刀 2：布]："))
computer=random.randint(0,2)
if person==0 and computer==1:
    print("您赢了")
    pass
elif person==1 and computer==2:
    print("您赢了")
    pass
elif person==2 and computer==0:
    print("您赢了")
    pass
elif person==computer:
    print("平手了")
    pass
else:
    print("您输了")
    pass

import random
count=1;
while count<=5:
    person=int(input("请出拳：[0:石头 1：剪刀 2：布]："))
    computer=random.randint(0,2)
    if person==0 and computer==1:
        print("您赢了")
        pass
    elif person==1 and computer==2:
        print("您赢了")
        pass
    elif person==2 and computer==0:
        print("您赢了")
        pass
    elif person==computer:
        print("平手了")
        pass
    else:
        print("您输了")
        pass
    count+=1


index = 1
while index <= 100:
    print(index)
    index += 1
    pass
