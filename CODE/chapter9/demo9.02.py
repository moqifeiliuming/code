class WarpdriveOverloadException(Exception):
    pass

warpSpeed = 12

if warpSpeed >= 10:
    raise WarpdriveOverloadException("曲速引擎已经过载，请停止或弹出曲速核心，否则飞船将会爆炸")