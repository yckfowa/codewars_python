import math
def nb_year(p0, percent, aug, p):
    count = 0
    increment = p0
    while(increment < p):
        increment = increment + math.floor(increment * (percent / 100)) + aug
        count += 1
    return count

