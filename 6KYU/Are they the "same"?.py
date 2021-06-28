def comp(array1, array2):
    if array2 == None or array1 == None:
        return False
    for each in array1:
        if each**2 in array2:
            array2.remove(each**2) # if both the items in arrays are the same, remove the element in array2 
    if len(array2) != 0:
        return False
    else:
        return True
