def high_and_low(numbers):
    list = []
    for n in numbers.split():
        list.append(int(n))
        highest = max(list)
        lowest = min(list)
    return f'{highest} {lowest}'
