
roman_re = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X',9: 'IX', 5: 'V', 4: 'IV', 1: 'I'} #specific values were added to avoid breaking 3 identifcal symbol in a row 

def solution(n):
    results = ""
    for key in roman_re.keys():
        while n >= key:
            results += roman_re[key]
            n -=key

    return results
