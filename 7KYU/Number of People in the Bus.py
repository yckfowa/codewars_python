#ver.1
def number(bus_stops):
    first_total = 0
    sec_total = 0

    for i in range(0, len(bus_stops)):
        first_total += bus_stops[i][0]
        sec_total += bus_stops[i][1]
    return first_total - sec_total

---------------------------------------
#ver.2 quicker way 

def number(bus_stops):
    return sum([stop[0] - stop[1] for stop in bus_stops])
