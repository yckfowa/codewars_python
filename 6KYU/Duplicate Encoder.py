def duplicate_encode(word):
    word = word.lower()

    return "".join(["(" if word.count(ch) == 1 else ")" for ch in word])
