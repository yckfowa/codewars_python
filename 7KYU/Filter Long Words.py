def filter_long_words(sentence, n):
    list = []
    for i in sentence.split():
        if len(i)> n:
            list.append(i)
    return list

