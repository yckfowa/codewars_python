def high(x):
    x = x.split()
    max_score = 0
    for el in x:
        score = 0
        for letter in el:
            score += (ord(letter) - 96)
        if score > max_score:
            max_score = score
            answer = el
    return answer
