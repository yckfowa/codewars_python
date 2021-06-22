def divisors(integer):
    list = []

    for i in range(2, int(integer/2) +1 ):
        if integer % i ==0:
            list.append(i)
    return list

    if len(list) == 0:
        return f'{integer} is prime'
