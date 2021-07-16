"""
returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.
"""

from collections import Counter

def scramble(s1, s2):
    return len(Counter(s2)-Counter(s1)) == 0

 # Counter creates a dictionary to store the count of each letter as key-value pair 
 # If the difference is an empty Counter, means the s1 Counter has excessive letters (and counts), and s2 can be made from some or all of the s1.
 # substractions are only allow in Counter not in dictionary

