def delete_nth(order, max_e):
    list = []
    for el in order:
        if list.count(el) < max_e:
            list.append(el)
    return list
