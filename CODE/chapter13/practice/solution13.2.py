import re
f = open('words.txt','r')
words = f.read()
wordList = re.split('[ ,;]+', words)
countDict = {}
for word in wordList:
    if countDict.get(word) == None:
        countDict[word] = 1
    else:
        countDict[word] = int(countDict[word]) + 1
for (key,value) in countDict.items():
    print(key,'=',value)
f.close()