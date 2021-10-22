import os
f = open('./files/urls.txt','r+')
url = ''
while True:
    url = f.readline()
    url = url.rstrip()
    if url == '':
        break;
    else:
        print(url)
print('-----------')
f.seek(0)
print(f.readlines())

f.write('https://jiketiku.com' + os.linesep)
f.close()

f = open('./files/urls.txt','a+')
urlList = ['https://geekori.com' + os.linesep, 'https://www.google.com' + os.linesep]
f.writelines(urlList)
f.close()