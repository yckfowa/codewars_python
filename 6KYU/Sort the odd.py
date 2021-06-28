def sort_array(source_array):
    odd = [n for n in source_array if n % 2 ]
    odd = sorted(odd)

    new_list = []

    for n in source_array:
        if n % 2 !=0 :
            new_list.append(odd.pop(0)) # remove the (0)index element from odd list and append to new_list 
        else:
            new_list.append(n)
    return list(new_list)
