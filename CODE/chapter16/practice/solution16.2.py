import ftplib
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
host = 'localhost'
def download():
    try:
        f = ftplib.FTP(host)
  
    except Exception as e:
        print(e)
        return
    print('FTP服务器已经成功连接')
    try:
        f.login('lining','lining.flame')
    except Exception as e:
        print(e)
        return    
    print('FTP服务器已经成功登录.')
    f.cwd('Pictures')   
    print(f.retrbinary('RETR %s' % 'pic.png',open('/Users/lining/Desktop/download.png','wb').write))
    f.quit()
def sendEmail():
    sender='lntoto@126.com'    
    password = 'flame88flame'              
    to='282662997@qq.com'  
    ret=True
    try:
        msg = MIMEMultipart('related')
        msg['From'] = sender
        msg['To'] =  to 
        msg['Subject'] = '从FTP服务器下载的图像文件'   
        msgAlternative = MIMEMultipart('alternative')
        msg.attach(msgAlternative)
        mail_msg = '<img src="cid:image1">'
        msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))
 
        # 指定图片为当前目录
        fp = open('/Users/lining/Desktop/download.png', 'rb')
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
 

if __name__ == '__main__':
    download()
    ret=sendEmail()
    if ret:
        print("邮件发送成功")
    else:
        print("邮件发送失败")
