s1 = "Today is {}, the temperature is {} degrees."
print(s1.format("Saturday", 24))

s2 = "Today is {week}, the temperature is {degree} degrees."
print(s2.format(degree = 22, week ="Sunday"))

s3 = "Today is {week}, {}，the {} temperature is {degree} degrees."
print(s3.format("aaaaa", 12345, degree = 22, week ="Sunday"))

s4 = "Today is {week}, {1}，the {0} temperature is {degree} degrees."
print(s4.format("aaaaa", 12345, degree = 22, week ="Sunday"))

fullname = ["Bill", "Gates"]
print("Mr {name[1]}".format(name = fullname))

import math
s5 = "The {mod.__name__} module defines the value {mod.pi} for PI"
print(s5.format(mod = math))






