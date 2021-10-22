while True:
    try:
        x = int(input('请输入分子：'))
        y = int(input('请输入分母：'))
        value = x / y
        print('x / y is', value)         
    except Exception as e:
        print('不正确的输入：',e)
        print('请重新输入')
    else:
        break