s = "I not only like python, but also like kotlin."
table = s.maketrans("ak", "*$")
print(table)
print(len(table))

print(s.translate(table))

table1 = s.maketrans("ak", "$%", " ")
print(s.translate(table1))
