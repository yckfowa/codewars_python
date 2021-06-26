def persistence(n):
    if n < 10:
        return 0
    n_str = str(n)
    count = 1
    for i in n_str:
        count = count * int(i)
    return 1 + persistence(count)
