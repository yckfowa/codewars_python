def in_array(array1, array2):
    list = []
    for el in array1:
        for el2 in array2:
            if el in el2:
                list.append(el)
    return sorted(set(list))
  
  
# better solution imo to the according to the description
  
def in_array(array1, array2):
    list = []
    for el in array1:
        for el2 in array2:
            if el in el2 and el not in list: # put in 2nd condition to check if el already exist in the list 
                list.append(el)
    return sorted(list)
  
