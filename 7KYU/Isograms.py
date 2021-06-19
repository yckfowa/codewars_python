def is_isogram(string):
    string = string.lower()

    list = []

    for letter in string:
        if letter in list:
            return False
        list.append(letter)

    return True
