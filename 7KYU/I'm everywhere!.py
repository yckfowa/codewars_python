def i(word):
    vowels = 'aAeEiIoOuU'
    if len(word) == 0 or word.startswith("I") or word[0].islower():
        return 'Invalid word'

    count = 0
    for ch in word:
        if ch in vowels:
            count+=1
    if count >= len(word)-count :
        return 'Invalid word'

    return f"{'i'+word}"
