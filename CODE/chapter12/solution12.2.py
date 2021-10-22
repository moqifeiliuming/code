from datetime import *

while True:
    try:
        d1 = input('请输入第1个日期：');
        d1 = datetime.strptime(d1, '%Y-%m-%d')
        d2 = input('请输入第2个日期：');
        d2 = datetime.strptime(d2, '%Y-%m-%d')
        d = d2 - d1
        print('两个日期之间相距%d天' % d.days)
    except Exception as e:
        print(e)


