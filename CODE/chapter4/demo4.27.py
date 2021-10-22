s = ["hello", "world","yeah"]
s[1:] = ["a","b","c"]            # 将列表s从第2个元素开始替换成一个新的列表
print(s)                        # 运行结果：['hello', 'a', 'b', 'c']
name = list("Mike")            # 使用list函数将“Mike”转换成由字符组成的列表
print(name)                    # 运行结果：['M', 'i', 'k', 'e']
name[1:] = list("ary")            # 利用分片赋值操作将“Mike”替换成了“Mary”    
print(name)                    # 运行结果：['M', 'a', 'r', 'y']
