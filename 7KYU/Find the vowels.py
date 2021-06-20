def vowel_indices(word):
    vowels = 'aAeEiIoOuUyY'
    list = []

    for x,letter in enumerate(word):
        if letter in vowels:
            list.append(x+1)
    return list
