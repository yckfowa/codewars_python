"""
Given a word and a list, locate the aragram of the word and return it/them in a list, if theres's none turn empty list

"""

def anagrams(word, words):

    lst = []
    for el in words:
        if sorted(el) == sorted(word):
            lst.append(el)
    return lst
  
 -----------------------------

def anagrams(word, words):
  
    return [el for el in words if sorted(el) == sorted(word)]
