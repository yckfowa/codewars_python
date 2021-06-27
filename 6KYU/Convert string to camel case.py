def to_camel_case(text):

    text = text.replace('_','-')
    t = text.split('-')

    for i in range(1,len(t)):
         t[i] = t[i].capitalize()
    return ''.join(t)



