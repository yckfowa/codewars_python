def first_non_consecutive(arr):
    i = 1
    for el in arr:
        if i <len(arr) and arr[i] - arr[i-1] != 1 :
            return arr[i]
        i += 1
    return None

