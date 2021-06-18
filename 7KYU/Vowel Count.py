def get_count(input_str):
    num_vowels = 0
    vowels = 'aeiou'

    for ch in input_str.lower():
        if ch in vowels:
            num_vowels +=1
    return num_vowels
