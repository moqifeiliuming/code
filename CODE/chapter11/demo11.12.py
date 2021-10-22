# 常用的正则表达式

import re
# Email
email = '[0-9a-zA-Z]+@[0-9a-zA-Z]+\.[a-zA-Z]{2,3}'
result = re.findall(email, 'lining@geekori.com')
print(result)
result = re.findall(email, 'abcdefg@aa')
print(result)
result = re.findall(email, '我的email是lining@geekori.com，不是bill@geekori.cn，请确认输入的Email是否正确')
print(result)



ipv4 = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
result = re.findall(ipv4, '这是我的IP地址：33.12.54.34，你的IP地址是100.32.53.13吗')
print(result)

url = 'https?:/{2}\w.+'
url1 = 'https://geekori.com'
url2 = 'ftp://geekori.com'
print(re.match(url,url1))
print(re.match(url,url2))
