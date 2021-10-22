import time

localtime = time.localtime(time.time())
print ("本地时间为 :", localtime)
print('年','=', localtime.tm_year)
print('月','=', localtime.tm_mon)
print('日','=', localtime.tm_mday)
print('一周的第%d' % localtime[7])
localtime = time.asctime( time.localtime(time.time()) )
print ("本地时间为 :", localtime)

