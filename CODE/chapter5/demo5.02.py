#  定义字符串模板
formatStr = "Hello %s. Today is %s, Are there any activities today?"
#  初始化字符串模板参数值，此处必须使用元组，不能使用列表
values = ('Mike', 'Wednesday')
#  格式化字符串
print(formatStr % values)
