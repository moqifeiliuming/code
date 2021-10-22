import random
import os

strList = ['abc','bbb',30,'xyz','ddd','ok','666']
dirs = random.sample(strList, 3)
print(dirs)
dirStr = ''
for dir in dirs:
    dir += os.sep
    dirStr += dir 
print(dirStr)
os.makedirs(dirStr, exist_ok=True)

