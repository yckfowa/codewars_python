def wave(people):
    lst = []
    for n in range(len(people)):
        temp = list(people)
        if temp[n].isalpha():
            temp[n]=people[n].upper()
            str= "".join(temp)
            lst.append(str)
    return lst
