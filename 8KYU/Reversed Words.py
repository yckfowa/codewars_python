def reverse_words(s):
    s_arr = []
    for ch in s.split(' '):
        s_arr.append(ch)
    return ' '.join(reversed(s_arr))

