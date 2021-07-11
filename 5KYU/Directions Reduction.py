"""
reduce the path that will get you nowhere and provide a simple path.
"""

def dirReduc(arr):

    directions = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}

    lst = []
    for el in arr:
        if lst and lst[-1] == directions[el]: # if list is not empty, and the added item isn't the opposite of last one added
            lst.pop()
        else:
            lst.append(el)
    return lst
