scope = {}
codes = ""
print(">>>",end="")
while True:
    code= input("")
    if code == "":
        exec(codes, scope)
        codes = ""
        print(">>>",end="")
        continue   
    codes += code + "\n"
