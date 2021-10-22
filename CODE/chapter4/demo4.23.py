account = [                        # 保存了多条用户记录的序列
    ["geekori", "123456"],
    ["bill", "54321"],
    ["superman", "65432"],
    ["androidguy","6543"],
    ["mike435", "65abcd"]
]

username = input("用户名：")            # 要求输入用户名
password = input("密码：")            # 要求输入密码
# 用in运算符判断一个序列是否属于account
if [username, password] in account:
    print("登录成功")
else:
    print("登录失败")
