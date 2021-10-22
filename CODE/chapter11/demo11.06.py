import re
# abc aabc   abbbccc
s = 'a+b+c+'
strList = ['abc','aabc','bbabc','aabbbcccxyz']
for value in strList:    
    m = re.match(s, value)
    if m is not None:
        print(m.group())
    else:
        print('{}不匹配{}'.format(value,s))

print('--------------')

# 任意3个数字-任意3个小写字母  
# 123-abc   433-xyz
#s = '\d\d\d-[a-z][a-z][a-z]'
s = '\d{3}-[a-z]{3}'  
strList = ['123-abc','432-xyz','1234-xyz','1-xyzabc','543-xyz^%ab']
for value in strList:    
    m = re.match(s, value)
    if m is not None:
        print(m.group())
    else:
        print('{}不匹配{}'.format(value,s))
print('-------------')
s = '[a-z]?\d+'
strList = ['1234','a123','ab432','b234abc']
for value in strList:    
    m = re.match(s, value)
    if m is not None:
        print(m.group())
    else:
        print('{}不匹配{}'.format(value,s))

print('-------------')
# email
email = '\w+@(\w+\.)*\w+\.com'
emailList = ['abc@126.com','test@mail.geekori.com','test-abc@geekori.com','abc@geekori.com.cn']
for value in emailList:    
    m = re.match(email,value)
    if m is not None:
        print(m.group())
    else:
        print('{}不匹配{}'.format(value,email))
strValue = '我的email是lining@geekori.com，请发邮件到这个邮箱'
m = re.search(email, strValue)
print(m)
email = '[a-zA-Z0-9]+@(\w+\.)*\w+\.com'
m = re.search(email, strValue)
print(m)


