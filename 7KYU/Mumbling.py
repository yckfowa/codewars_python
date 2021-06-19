def accum(s):
    s = list(s)

    result = ""
    j = 0
    for i in s:
        j += 1
        i = i*j
        i = i.title()
        result = result + i + '-'

    result = result.strip("-")

    return result
