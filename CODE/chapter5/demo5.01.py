s1 = "hello world"
#  在字符串中使用索引
print(s1[0])                # 获取s1的第1个字符，运行结果：h
print(s1[2])                # 获取s1的第3个字符，运行结果：l
#  在字符串中使用分片
print(s1[6:9])                    # 获取s1从第7个字符往后的3个字符，运行结果：wor
print(s1[6:])                # 获取s1从第7个字符后的所有字符，运行结果：world
print(s1[::2])                # 在s1中每隔一个取一个字符，运行结果：hlowrd

s2  = "abc"
#  在字符串中使用乘法
print(10 * s2)                #  运行结果：abcabcabcabcabcabcabcabcabcabc
print(s2 * 5)                #  运行结果：abcabcabcabcabc
#  在字符串中使用in运算符
print('b' in s2)            #  运行结果：True
print('x' not in s2)        #  运行结果：True

print(len(s1))                #  获取s1的长度，运行结果：11
print(min(s2))                #  获取s2中按ASCII计算最小的字符，运行结果：a
print(max(s2))                #  获取s2中按ASCII计算最大的字符，运行结果：c
