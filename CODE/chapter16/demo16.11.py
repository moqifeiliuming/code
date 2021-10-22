import smtplib
from email.mime.text import MIMEText
sender ='发送者的EMail地址'    
password = '发送者的EMail密码'              
to ='接收者的EMail地址' 
def mail():
    ret=True
    try:
        
        msg=MIMEText('这是第一封email','plain','utf-8')
        msg['From']=sender 
        msg['To']=to            
        msg['Subject']="这是欧瑞学院（https://geekori.com/edu）发送的一封邮件"

        # SMTP("smtp.126.com", 25) 
        server=smtplib.SMTP_SSL("smtp.126.com", 465)  
        server.login(sender, password)  # 括号中对应的是发件人邮箱账号、邮箱密码
        print(msg.as_string())
        server.sendmail(sender,[to,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret=False
        print(e)
    return ret
 
ret=mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")