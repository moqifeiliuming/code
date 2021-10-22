import time

time1 = time.time()
time2 = time1 + 60             # 1分钟
time3 = time1 + 60 * 60         # 1小时
time4 = time1 - 60 * 60 * 24    # 1天
time1 = time.localtime(time1)
time2 = time.localtime(time2)
time3 = time.localtime(time3)
time4 = time.localtime(time4)
print (time.strftime("%Y-%m-%d %H:%M:%S", time1))
print (time.strftime("%Y-%m-%d %H:%M:%S", time2))
print (time.strftime("%Y-%m-%d %H:%M:%S", time3))
print (time.strftime("%Y-%m-%d %H:%M:%S", time4))

