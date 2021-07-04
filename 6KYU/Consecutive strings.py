def longest_consec(strarr, k):
    lst = []
    if k > 0 and len(strarr)>= k:
        for i in range(len(strarr)):
            n = ''.join(strarr[i:i+k])
            lst.append(n)
        return max(lst, key=len)
    else:
        return ''
