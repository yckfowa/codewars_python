def solution(s):
    res = ""

    for el in s:
        if el.isupper():
            res += ' ' + el
        else:
            res +=el
    return res
