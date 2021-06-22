def number(bus_stops):
    first_total = 0
    sec_total = 0

    for i in range(0, len(bus_stops)):
        first_total += bus_stops[i][0]
        sec_total += bus_stops[i][1]
    return first_total - sec_total
