"""
adding hastag for the string given, if the result is more than 140 return false, empty input or result also return false
"""


def generate_hashtag(s):
    s1 = "#" + s.title().replace(" ","")

    if len(s)> 140 or s =="":
        return False
    return s1

