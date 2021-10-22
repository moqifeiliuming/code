# 输出带“\n"的字符串，运行结果：<hello
 #                            world>
print("<hello\nworld>")
# 用str函数将1234转换为数字，运行结果：1234
print(str(1234))
#  抛出异常，len函数不能直接获取数字的长度
#print(len(1234))   
#  将1234转换为字符串后，获取字符串长度，运行结果：4
print(len(str(1234)))
#  运行结果：<hello
 #            world>
print(str("<hello\nworld>"))
#  运行结果：13
print(len(str("<hello\nworld>")))
#  运行结果：'<hello\nworld>'
print(repr("<hello\nworld>"))
#  运行结果：16
print(len(repr("<hello\nworld>")))
print("<hello\\nworld>")
print(len("<hello\\nworld>"))
print(r"<hello\nworld>")
print(len(r"<hello\nworld>"))

