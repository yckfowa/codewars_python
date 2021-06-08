def abbrev_name(name):
    name = name.split()
    abbre =[]
    for ch in name:
        abbre.append(ch[0].upper())
    return '.'.join(abbre)
