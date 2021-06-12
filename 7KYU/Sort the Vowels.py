#credit to ZaytsevNS for the inspriation 

def sort_vowels(s):
    if type(s) != str:
       return ''
    vowels = 'AaEeIiOoUu'
    s_new_format = ''
    nl = '\n'
    for ch in s:
        if ch not in vowels:
            s_new_format += f'{ch + "|" + nl}'
        else:
            s_new_format += f'{"|" + ch + nl}'
    return s_new_format[:-1]
