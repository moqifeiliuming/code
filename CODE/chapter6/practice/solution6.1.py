import random
dict= {}
for key in range(0,1000):
    dict.setdefault(random.randint(0,100), key * key)

print(dict.items())

