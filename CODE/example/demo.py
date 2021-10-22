height = float(input("请输入您的身高："))
print("您的身高是：%height"%height)
weight = float(input("请输入您的体重："))
print("您的体重是："+str(weight))
BMI = weight / (height * height)
print("您的BMI值是："+str(BMI))
print("您的BMI值是："+str(BMI))   #str()是将数值转换为字符串
if BMI < 18.5:
    print("您的体重过轻")
elif 18.5 <= BMI <= 24.9:
    print("您的体重正常")
elif 24.9 <= BMI <= 29.9:
    print("您的体重偏胖")
elif BMI > 29.9:
    print("您的体重超标")

print("计算1+2+3+......+100的结果为")
sum = 0
for i in range(1,101):
    sum += i
print(sum)
