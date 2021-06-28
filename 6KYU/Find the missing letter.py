import string

def find_missing_letter(chars):
    charset = string.ascii_lowercase if chars[0] >= 'a' else string.ascii_uppercase # to determine whether to use lowercase or uppercase 
    for letter in charset[charset.index(chars[0]):]:
        if letter not in chars:
            return letter[0]
