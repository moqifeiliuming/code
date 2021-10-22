from heapq import *
from random import *

data = [1, 2, 3, 4, 5, 6,7,8,9]
heap = []
for n in data:
    value = choice(data)
    heappush(heap,value)
print(heap)
heappush(heap,2.5)
print(heap)
print(heappop(heap))
print(heap)
data1 = [6,3,1,12,8]
heapify(data1)
print(data1)


heapreplace(data1, 100)
print(data1)

print(nlargest(1,data1))
print(nlargest(2,data1))
print(nsmallest(1,data1))
print(nsmallest(3,data1))

print(list(merge([1,3,5,7], [0,2,4,8], [5,10,15,20], [], [25])))


print(list(merge(['dog', 'horse'], ['cat', 'fish', 'kangaroo'], key=len)))
