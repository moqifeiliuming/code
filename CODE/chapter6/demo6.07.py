newDict1 = {}.fromkeys(['name', 'company','salary'])
print(newDict1)

newDict2 = newDict1.fromkeys(('name', 'company','salary'))
print(newDict2)

newDict3 = newDict1.fromkeys(['name', 'company','salary'],'没有值')
print(newDict3)