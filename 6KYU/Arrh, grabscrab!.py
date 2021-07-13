"""
Pirates have notorious difficulty with enunciating. They tend to blur all the letters together and scream at people.

At long last, we need a way to unscramble what these pirates are saying.

Write a function that will accept a jumble of letters as well as a dictionary, and output a list of words that the pirate might have meant.

"""


def grabscrab(word, possible_words):
    
    return [ch for ch in possible_words if sorted(ch) == sorted(word)]

