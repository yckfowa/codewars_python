# research made on stackoverflow
from string import ascii_lowercase # to have a-z instead of hacoding it down

LETTERS = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)} # set the condition where enumerate starts with 1:a to meet the requirment 

def alphabet_position(text):
    text = text.lower()
    numbers = [LETTERS[character] for character in text if character in LETTERS] #return the number of position of the alphabet and join with space 
    return ' '.join(numbers)
