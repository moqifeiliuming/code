dict = {'name':'Bill', 'age':40}
try:
    print(dict['Age'])
except KeyError as e:
    print("异常信息：{}".format(e))
class WifiManager:
    def testWifi(self):
        print("testWifi")

wifiManager = WifiManager()
try:
    wifiManager.testWiFi()
except AttributeError as e:
    print("异常信息：{}".format(e))
