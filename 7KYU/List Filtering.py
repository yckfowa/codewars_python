#remove method only removes one single value, not applicable

def filter_list(l):
    list = []

    for ch in l:
        if type(ch) is not str:
            list.append(ch)
    return list


