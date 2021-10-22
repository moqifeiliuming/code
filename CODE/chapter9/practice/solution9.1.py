class StartMobileException(Exception):
    pass
import random
class Mobile:
    
    def start(self):
        value = random.randint(1,100)
        if value < 50:
            raise StartMobileException('开机错误')

mobile = Mobile()
mobile.start()
                              