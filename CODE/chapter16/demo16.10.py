import ftplib

host = 'localhost'
def dirCallback(dir):
    print(dir.encode('ISO-8859-1').decode('utf-8'))
def main():
    try:
        f = ftplib.FTP(host)
  
    except Exception as e:
        print(e)
        return
    print('FTP服务器已经成功连接')
    try:
        f.login('用户名','密码')
    except Exception as e:
        print(e)
        return    
    print('FTP服务器已经成功登录.')
    f.cwd('Pictures')
    f.dir(dirCallback)
    print('当前工作目录：',f.pwd())
    try:
        f.mkd('新目录'.encode('GBK').decode('ISO-8859-1'))
        f.cwd('新目录'.encode('GBK').decode('ISO-8859-1'))
        f.mkd('dir1')
        f.mkd('dir2')
    except:
        f.cwd('新目录'.encode('utf-8').decode('ISO-8859-1'))
        
    print('-----')

   
    upload_file = '/Users/lining/Desktop/a.png'
    ff = open(upload_file,'rb')
    
    print(f.storbinary('STOR %s' % 'a.png',ff))
    f.dir(dirCallback)

    print(f.retrbinary('RETR %s' % 'a.png',open('/Users/lining/Desktop/xx.png','wb').write))
    f.quit()
    
if __name__ == '__main__':
    main()