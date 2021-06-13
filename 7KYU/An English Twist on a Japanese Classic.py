def game(words):
    for i in range(len(words)-1):
        if words[i] == '':
            return words[:i]
        if words[i][-1:] != words[i+1][:1]:
            return words[:i+1]
