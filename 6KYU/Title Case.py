
title_case(title, minor_words=''):
    title = title.capitalize().split()  # ensure the rest of the word are lower except the first word in the title
    minor_words = minor_words.lower().split()
    return ' '.join(words if words in minor_words else words.capitalize() for words in title) 
