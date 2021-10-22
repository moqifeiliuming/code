import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
sender ='发送者的EMail地址'    
password = '发送者的EMail密码'              
to ='接收者的EMail地址'  
def mail():
    ret=True
    try:
 
        msg = MIMEMultipart('related')
        msg['From'] = sender
        msg['To'] =  to 
        msg['Subject'] = '欧瑞学院（带附件）'   
 
        msgAlternative = MIMEMultipart('alternative')
        msg.attach(msgAlternative)
        mail_msg = """
        <p>欧瑞学院祝贺广大学员更上一层楼.</p>
        <p><a href="https://geekori.com/edu">欧瑞学院</a></p>
        <p>图片演示：</p>
        <p><img src="cid:image1"></p>
        """
        msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))
 
        # 指定图片为当前目录
        fp = open('/Users/lining/Desktop/xx.png', 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()
 
        # 定义图片 ID，在 HTML 文本中引用
        msgImage.add_header('Content-ID', '<image1>')
        msg.attach(msgImage)
        server=smtplib.SMTP_SSL("smtp.126.com", 465)  
        server.login(sender, password)  # 括号中对应的是发件人邮箱账号、邮箱密码
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