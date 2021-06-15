def strange_math(n,k):
    list = []
    for i in range(1, n+1):
        list.append(str(i))
    list.sort()

    return (list.index(str(k)))+1
