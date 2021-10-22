import imaplib
import base64
connection = imaplib.IMAP4_SSL('imap.qq.com', 993)


username = '邮箱用户名'
password = '邮箱密码'
 
# 登陆
try:
    connection.login(username, password)
except Exception as err:
    print('登陆失败: :', err)  # 输出登陆失败的原因
 
# 输出日志
connection.print_log()
res,data = connection.list()
print('Response code:', data)

    
res, data = connection.select('INBOX')

print(res, data)
print(data[0])  # 邮件数

res, msg_ids = connection.search(None, 'ALL')  # 你也可以直接搜索邮件
print(res, msg_ids)
res, msg_data = connection.fetch(data[0], '(UID BODY[TEXT])') # '(UID BODY[TEXT])'  '(BODY.PEEK[TEXT])'
print(msg_data)
connection.logout()