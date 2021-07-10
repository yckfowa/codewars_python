"""
Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. 
The function should return true if the string is valid, and false if it's invalid.
"""

def valid_parentheses(string):
    count = 0

    for ch in string:
        if ch == "(":
            count += 1
        elif ch == ")":
            count -= 1

        if count < 0:
            return False
    return count == 0
