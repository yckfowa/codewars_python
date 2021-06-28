def narcissistic(value):
    total = 0
    list = str(value)
    list_length = len(list)
    for i in range(0,list_length):
        total += pow(int(list[i]),list_length)
    if value == total:
        return True
    else:
        return False
