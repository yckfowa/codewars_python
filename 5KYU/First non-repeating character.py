"""
write a function to return the first non-repeating character, uppercase and lowercase should consider the same character but h
but have the return the original character, if contains all repeating characters, return empty string
"""


def first_non_repeating_letter(string):

    lst = [i.lower() for i in string]
    for i in range(len(lst)):
        if lst.count(lst[i]) == 1:
            return string[i]
    return ""
