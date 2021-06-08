def sp_eng(sentence):
    english = ["ENGLISH", "english"]

    if english[0] in sentence.upper():
        return True
    elif english[1] in sentence.lower():
        return True
    return False
