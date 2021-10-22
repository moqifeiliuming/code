print("{0:=^10.2f}".format(-4.56))

from math import pi
print("{pi:012.3f}".format(pi = pi))
numStr = input("请输入章节序号的位数：")
num = int(numStr)
print("第{:0{num}.0f}章，第{:03.0f}节".format(1,2,num = num))
print('{0:<10.2f}\n{0:^10.2f}\n{0:>10.2f}'.format(pi))
print("{:$^20}".format(" 美元 "))
print("{:￥<20}".format(" 人民币 "))
print("{0:=10.2f}".format(-pi))
sign = input("请输入在数值前面输出的符号：")
print("{0:{sign}=10.2f}".format(-pi,sign = sign))
numStr = input("请输入要转换为二进制和十六进制的数：")
num = int(numStr)
print("{:b}".format(num))
print("{:#b}".format(num))
print("{:x}".format(num))
print("{:#x}".format(num))




