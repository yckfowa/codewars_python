"""
count the number of times a character shows up in the string and output it as a dictionary
"""

def count(string):
    new_dict = {}

    for ch in string:
        if ch not in new_dict:
            new_dict[ch] = 1
        else:
            new_dict[ch] += 1
    return new_dict

  -------------------------------
# 2nd solution 
from collections import Counter as count

def count(string):
  return {i: string.count(i) for i in string}
