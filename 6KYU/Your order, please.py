def order(sentence):
    sentence = sentence.split()
    sentence.sort(key=min)
    return ' '.join(sentence)
