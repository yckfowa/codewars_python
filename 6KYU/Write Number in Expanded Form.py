def expanded_form(num):
    result = []

    for index, digit in enumerate(str(num)[::-1]): #reverse the string to get the right sequence of index accordingly
        if int(digit) != 0:
            result.append(digit + ('0' * index))
        
    return ' + '.join(result[::-1])
