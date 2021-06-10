def is_vow(s):
    vowels = {97: 'a', 111: 'o', 117: 'u', 101: 'e', 105: 'i'}
    list =[]
    for el in s:
        if el in vowels.keys():
            el = vowels[el]
        list.append(el)

    return list


