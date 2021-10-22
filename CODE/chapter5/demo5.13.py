print("HEllo".lower())
print("hello".upper())
list = ["Python", "Ruby", "Java", "KOTLIN"]
if "Kotlin" in list:
    print("找到Kotlin了")
else:
    print("未找到Kotlin")

for lang in list:
    if "kotlin" == lang.lower():
        print("找到Kotlin了")
        break;
s = "i not only like Python, but also like Kotlin."
import string
print(string.capwords(s))