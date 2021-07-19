"""
Given a year, return the century it is in.
"""

def century(year):
    if year <= 100:
        return 1
    elif year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1
