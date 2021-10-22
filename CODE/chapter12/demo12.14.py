import calendar
import locale

cal = calendar.month(2017, 1)

print(cal);

locale.setlocale(locale.LC_ALL, 'zh_CN.UTF-8')

cal = calendar.month(2017, 1)

print(cal);
locale.setlocale(locale.LC_ALL, '')
print(calendar.calendar(2017))

