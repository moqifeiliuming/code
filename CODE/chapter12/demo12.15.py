import random
print(random.randint(1,100))
print(random.random())
# [1,4,7,10,13,16,19]选一个
print(random.randrange(1, 20, 3))
print(random.uniform(1, 100.5))
intList = [1,2,3,4,5,6,7,8,9,'a','b','c','d']
print(random.choice(intList))
newList = random.sample(intList, 3) 
print(newList)
random.shuffle(intList)
print(intList)
