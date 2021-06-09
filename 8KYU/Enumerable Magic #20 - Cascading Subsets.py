def each_cons(lst, n):
    list = []
    for i in range(len(lst)-n+1):
        list.append(lst[i:i+n])
    return list
