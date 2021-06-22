# Do not mutate the original list, hence copy() was used 

def remove_smallest(numbers):
    numbers = numbers.copy()
    if len(numbers) < 1 :
        return numbers
    else:
        numbers.remove(min(numbers))
        return numbers

