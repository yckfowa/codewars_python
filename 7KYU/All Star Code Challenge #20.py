def add_arrays(array1, array2):

    list =[]
    if len(array1) == len(array2):
        for i in range(0, len(array1)):
            list.append(array1[i]+array2[i])
        return list 
    return Error
