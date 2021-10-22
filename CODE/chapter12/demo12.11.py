import time
import locale
locale.setlocale(locale.LC_ALL, 'zh_CN.UTF-8')
# 格式化成2016-03-20 11:45:39形式
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

print (time.strftime("%Y年%m月%d日 %H时%M分%S秒", time.localtime()))
print(time.strftime('%Y{y}%m{m}%d{d} %H{H}%M{M}%S{S}').format(y='年', m='月', d='日',H='时', M='分', S='秒'))

print(time.strftime('今天是%A',time.localtime()))