def dig_pow(n, p):

    number_split = [int(el) for el in str(n)]
    total = 0
    for i, p in enumerate(number_split, start=p):
        total += (p**i)
    total

    return total // n if (total % n) == 0 else -1


