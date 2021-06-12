def last_survivor(letters, coords):
    lst = list(letters)
    for pos in coords:
        lst.pop(pos)
    return ''.join(lst)
