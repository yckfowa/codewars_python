def zero_fuel(distance_to_pump, mpg, fuel_left):
    return True if fuel_left >= distance_to_pump/mpg else False
 
