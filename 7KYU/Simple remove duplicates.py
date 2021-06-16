def solve(arr): 
    duplicates = []
    for i in arr[::-1]:
        if i not in duplicates:
            duplicates.append(i)
    return duplicates[::-1]
