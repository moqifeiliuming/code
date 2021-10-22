def enumList(nestedList):
    try:
        try: nestedList + ''
        except TypeError:
            pass
        else:
            raise TypeError
        for subList in nestedList:
           for element in enumList(subList):
                yield element
    except TypeError:
        yield nestedList
nestedList = ['a',['b',['c'],20,123,[['hello world']]]]
for num in enumList(nestedList):
    print(num, end=' ')
