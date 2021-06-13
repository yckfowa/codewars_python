def even_last(numbers):
    total = 0
    
    if len(numbers) == 0:
        return 0
    
    for i in range(0, len(numbers)):
        if i == 0 or i % 2 == 0:
            total += numbers[i]

    return total* numbers[-1]
