def disemvowel(string_):

    vowels = 'aAeEiIoOuU'
    results = [ch for ch in string_ if ch not in vowels]
    return ''.join(results)
  
  
