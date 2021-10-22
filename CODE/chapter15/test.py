from socket import *
import re
from time import ctime
import os
def responseHeaders(file,length):
    f = open(file,'r')
    
    headersText = f.read()
    headersText = headersText % length
    return headersText


def filePath(get):
    if get == '/':
        return 'static' + os.sep + 'index.html'
    else:
        paths = get.split('/')
        s = 'static'
        for path in paths:
            if path.strip() != '':
                s = s + os.sep + path 
        return s
    
print(os.path.exists('a'))
        