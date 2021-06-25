def duplicate_count(text):
    text = text.lower()
    list = []
    for ch in text:
        if text.count(ch) > 1:
           list.append(ch)
    return len(set(list))
