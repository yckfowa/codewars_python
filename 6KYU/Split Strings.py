"""
Splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').
"""
def solution(s):
    lst = []
    for i in range(len(s)):
        if len(s) % 2 != 0:
            s = s + "_"
        if i % 2 == 0:
            lst.append(s[i:i + 2])

    return lst
  
------------------------------------

#regex ver.

import re

def solution(s):
    return re.findall(".{2}", s + "_")
