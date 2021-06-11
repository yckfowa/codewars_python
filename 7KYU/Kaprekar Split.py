def kaprekar_split(n):
    sqr = str(n**2)
    if len(sqr) == 1:
        return 0
    for i in range(1, len(sqr)):
        if int(sqr[:i]) + int(sqr[i:]) == n:
            return i

    return -1
