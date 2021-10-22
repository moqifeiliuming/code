def search(sequence, number, lower = 0, upper = None):
    if upper is None: upper = len(sequence) - 1
    if lower == upper:
        if number == sequence[upper]:
            return upper
        else:
            return -1
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return search(sequence, number, middle + 1, upper)
        else:
            return search(sequence, number, lower, middle)
list = [1,4,6,8,9,12,45,97]
print(search(list, 9))
print(search(list, 15))