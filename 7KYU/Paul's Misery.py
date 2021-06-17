def paul(x):
    dic = {'kata': 5, 'Petes kata': 10, 'life': 0, 'eating': 1}

    score = 0
    for k in x:
        if k in dic:
            score += dic.get(k)

    if score < 40:
        return 'Super happy!'
    elif 40 <= score < 70:
        return 'Happy!'
    elif 70<= score < 100:
        return 'Sad!'
    else:
        return 'Miserable!'
