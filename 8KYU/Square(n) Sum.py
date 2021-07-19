"""
Complete the square sum function so that it squares each number passed into it and then sums the results together.
"""

def square_sum(numbers):
    total = 0
    for n in numbers:
        sqr = n**2
        total += sqr
    return total
