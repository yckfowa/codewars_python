# reverse() method reverse the element of a list
# * int cannot be iterate must transform into str

def digitize(n):
    array = []
    for el in str(n):
        array.append((int(el)))
    return list(reversed(array))

print(digitize(12321312))