def descending_order(num):
    reorder = "".join(sorted(str(num), reverse=True))
    return int(reorder)
