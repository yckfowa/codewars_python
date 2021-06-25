def spin_words(sentence):
    sentence = sentence.split()
    list = []

    for ch in sentence:
        if len(ch) >= 5:
            list.append(ch[::-1])
        else:
            list.append(ch)
    return " ".join(list)
