def count_name(arr, name):
    for i in arr:
        if name in arr:
            return arr.count(name)
