def unique_in_order(iterable):
    unique_list = []
    prev = None

    for ch in iterable:
        if ch != prev:
            unique_list.append(ch)
            prev = ch

    return unique_list
