def sortNumbers(*numbers,type="asc"):
    if type == "asc":
        return sorted(numbers)
    else:
        return sorted(numbers,reverse = True)

print(sortNumbers(6,5,3,8,4,3))
print(sortNumbers(6,5,3,8,4,3,type="desc"))
    