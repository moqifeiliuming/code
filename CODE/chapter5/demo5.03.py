# 在这个字符串模板中，包含在浮点数和整数类型的格式化参数
formatStr1 = "PI是圆周率,他的值是%.4f（保留小数点后%d位）"
#  导入math模块中的pi变量
from math import pi
#  定义与formatStr1对应的格式化参数值
values1 = (pi, 4)
#  格式化字符串，运行结果：PI是圆周率,他的值是3.1416（保留小数点后4位）
print(formatStr1 % values1)
#  在这个字符串模板中，包含了整数和字符串类型的格式化参数
formatStr2 = "这件事的成功率是%d%%, 如果有%s参与的话，成功率会提升至%d%%"
values2 = (56, "John",70)
#  运行结果：这件事的成功率是56%, 如果有John参与的话，成功率会提升至70%
print(formatStr2 % values2)
values3 = (66,"Mike")
#  由于指定的参数值的数量和格式化参数的数量不匹配，所以会抛出异常
print(formatStr2 % values3)
