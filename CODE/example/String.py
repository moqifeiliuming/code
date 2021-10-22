str1='我今天一共走了'
num=8000
str2='步'
#print(str1+num+str2)  #会报错，需要将整型数值改成字符串
print(str1+str(num)+str2)
print(str1+str(num)+'\n'+str2)
#汉字在GBK/GB2312编码中占2个字节，在UTF-8/unicode编码中占用3个字节（或者4个字节）

#截取字符串  string[start : end : step]   start(包括该字符)，end(不包括该字符)
#分割字符串是把字符串分割为列表，而合并字符串是把列表合并为字符串

str1='@明日科技 @扎克伯格 @俞敏洪'
list1 = str1.split()
print("您@的好友有：")
for item in list1:
    print(item[1:])

list2=['1','2','3']
str_list=' @'.join(list2)  #由于使用join()方法时，第一个元素前不加分隔符，所以需要在前面添加@符号
print(str_list)
at = '@'+str_list
print(at)

#find()方法：检索是否包含指定的子字符串，如果检索的字符串不存在，则返回-1
#rfind()方法：作用与find()方法类似，但是从字符串的右边开始查找
#index()方法：检索是否包含指定的子字符串，当不存在时会抛出异常
#startwith()方法：检索字符串是否以指定的子字符串开头，如果是返回True
#endwith()方法：检索字符串是否以指定的子字符串结尾，如果是返回True
#lower()方法：将字符串中的大写字母转换成小写字母
#upper()方法：将字符串中的小写字母转换成大写字母
#strip([chars])方法：用于去掉字符串左、右两侧的空格和特殊字符
#Istrip()方法：用于去掉字符串左侧的空格和特殊字符
#Rstrip()方法：用于去掉字符串右侧的空格和特殊字符

#str类型和bytes类型之间可以通过编码encode()和解码decode()方法进行转换，二者是互逆的过程
#在使用encode()、decode()方法时，不会修改原字符串，如果需要修改原字符串，则对其进行重新赋值
vers='野渡无人舟自横'
byte=vers.encode('GBK')
print("编码后的结果为：",byte)
print("解码后的结果为：",byte.decode('GBK'))  #此时需要与编码的格式一致

#正则表达式
#行定位符：^ 表示行的开始，$ 表示为行的结尾
# \bmr\w*\b  先从某个单词开始处(\b),匹配字母mr，接着是任意数量的字母或数字(\w*)，最后单词结束(\b)。可以匹配 'mrsoft','\nmr',但是不能与amr进行匹配
# 元字符
# .  匹配除换行符以外的任意字符
# \w 匹配字母、数字、下划线或者汉字
# \W 匹配字母、数字、下划线或汉字以外的字符
# \s 匹配单个的空白字符（包括Tab键和换行符）
# \S 匹配单个的空白字符（包括Tab键和换行符）以外的所有字符
# \b 匹配单词的开始或者结束，单词的分解符通常是空格，标点符号或者换行 在"I like mr or am"字符串中，\bm与mr中的m相匹配，但与am中的m不匹配
# \d 匹配数字

# 限定符
# ?     匹配前面的字符零次或一次
# +     匹配前面的字符一次或多次
# *     匹配前面的字符零次或多次
# {n}   匹配前面的字符n次
# {n,}  匹配前面的字符最少n次
# {n,m} 匹配前面的字符最少n次，最多m次

# 转义字符(\)是将特殊字符(如”.“ ”?“ ”\“)等变成普通的字符
# 括号在正则表达式中算是一个元字符
# 如果将匹配以字母m开头的单词的正则表达式转换为模式字符串，则不能直接在其两侧添加引号定界符，'\bm\w*\b'（是错误的）
# 而是要将其中的“\”进行转义，转换后的结果为：'\\bm\\w*\\b' 由于模式字符串中可能包括大量的特殊字符和反斜杠，
# 需要写为原生字符串，即在模式字符串前加r或者R，如上面的模式字符串可写成原生字符串为：r'\bm\w*\b'

# 常用标志
# A 或 ASCII         对于\w、\W、\b、\B、\d、\D、\s 只进行ASCII匹配（仅适用于python3.x)
# I 或 IGNORECASE    执行不区分字母大小写的匹配
# M 或 MULTILINE     将^和$用于包括整个字符串的开始和结尾的每一行（默认情况下，仅适用于整个字符串的开始和结尾处）
# S 或 DOTALL        使用(.)字符匹配所有字符，包括换行符
# X 或 VERBOSE       忽略模式字符串中未转义的空格和注释

import re
pattern=r'(13[4-9]\d{8})$|(15[01289]\d{8})$'
mobile='13645326413'
match=re.match(pattern,mobile)
if match == None:
    print(mobile,'不是有效的中国移动号码')
else:
    print(mobile,'是有效的中国移动号码')
mobile = '13144222221'
match=re.match(pattern,mobile)
if match == None:
    print(mobile,'不是有效的中国移动号码')
else:
    print(mobile,'是有效的中国移动号码')

# match()方法用于从字符串的开始处进行匹配，如果在起始位置匹配成功，则返回Match对象，否则返回None
import re
pattern = r'mr_\w+'
string = 'MR_SHOP mr_shop'
match = re.match(pattern,string,re.I)
print(match)
string = '项目名称MR_SHOP mr_shop'
match = re.match(pattern,string,re.I)
print(match)
print()

# search()方法进行匹配，用于整个字符串中搜索第一个匹配的值，如果匹配成功，则返回Match对象，否则返回None
import re
pattern = r'mr_\w+'
string = 'MR_SHOP mr_shop'
match = re.search(pattern,string,re.I)
print(match)
string = '项目名称MR_SHOP mr_shop'
match = re.search(pattern,string,re.I)
print(match)
string = '项目名称MH_SHOP mr_shop'   #找到了mr_shop,并返回此值
match = re.search(pattern,string,re.I)
print(match)

# findall()方法用于在整个字符串中搜索所有符合正则表达式的字符串，并以列表的形式返回。如果匹配成功，则返回包含匹配结构的列表，否则返回空列表
import re
pattern = r'mr_\w+'
string = 'MR_SHOP mr_shop'
match = re.findall(pattern,string,re.I)
print(match)
string = '项目名称MR_SHOP mr_shop'
match = re.findall(pattern,string)  #此时区分大小写
print(match)

# sub()方法用于实现字符串替换
# re.sub(pattern, rep1, string, count, flags)
import re
pattern = r'1[34578]\d{9}'
string = '中奖号码为：235343 联系电话为：13623434531'
result = re.sub(pattern,'1xxxxxxxxxx',string)
print(result)

# split()方法用于实现根据正则表达式分割字符串，并以列表的形式返回，其作用同字符串对象的split()方法类似，所不同的就是分割字符由模式字符串指定
# re.split(pattern,string,[maxsplit],[flags])
import re
pattern = r'[?|&]'
url = 'http://www.mingrisoft.com/login.jsp?username="mr"&password=mrsoft'
result = re.split(pattern,url)
print(result)

# 同时@三个好友
import re
str1='@明日科技 @扎克伯格 @俞敏洪'
pattern = r'\s*@'   #用空格和@或单独的@来分割字符串
list1 = re.split(pattern,str1)
print(list1)    #['', '明日科技', '扎克伯格', '俞敏洪']
print("您@的好友有：")
for item in list1:
    if item != "":
        print(item)
