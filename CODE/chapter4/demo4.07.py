# 将中文月份放到序列中
months = [
    '一月',
    '二月',
    '三月',
    '四月',
    '五月',
    '六月',
    '七月',
    '八月',
    '九月',
    '十月',
    '十一月',
    '十二月'
    ]
year = input("年：")                # 输入年
month = input('月（1-12）：')            # 输入月
day = input('日（1-31）：')            # 输入日

monthNumber = int(month)            # 将字符串形式的月转换为数值形式的月

monthName = months[monthNumber - 1]                    # 从序列中获取中文的月份
print(year + "年 " + monthName + " " + day + "日")        # 按指定格式输入年月日
