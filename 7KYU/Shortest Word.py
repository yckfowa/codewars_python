def find_short(s):
    list = s.split()
    l = sorted(list, key=len)
    return len(l[0])
