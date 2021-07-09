"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
"""


def pig_it(text):
    lst = []
    text = text.split()
    for ch in text:
        if ch.isalpha() is False:
            lst.append(ch)
        else:
            ch = ch[1:] + ch[0] + "ay"
            lst.append(ch)
    return " ".join(lst)
  
  --------------------------------------
 #list comprhension 
  
  def pig_it(text):
    return ' '.join([ch[1:]+ch[0]+'ay' if ch.isalpha() else ch for ch in text.split()])
