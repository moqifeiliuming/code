print("  geekori.com   ".strip())
print("  <   geekori.com   >  ".strip())

langList = ["python", "java", "ruby", "scala", "perl"]
lang = "  python  "
if lang in langList: 
    print("<找到了python>")
else:
    print("<未找到python>")
    
if lang.strip() in langList:
    print("{找到了python}")
else:
    print("{未找到python}")
    
print("***  &* Hello& *World**&&&".strip(" *&"))
    
