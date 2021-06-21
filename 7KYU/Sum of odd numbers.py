#ver1. 

def row_sum_odd_numbers(n):
    start = n * (n-1) + 1
    total = 0

    for i in range(n):
        total += start
        start += 2
    return total
----------------------------
#ver2. mathematic solution 

def row_sum_odd_numbers(n):
    return n ** 3
