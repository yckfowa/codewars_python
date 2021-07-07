
roman_de = {"I": 1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

def solution(roman):
    sum = 0
    for i in range(len(roman)):
        sum = sum + roman_de[roman[i]]
        if i > 0 and roman_de[roman[i]] > roman_de[roman[i - 1]]:  # for example 4 = IV, if value of V greater than value of I, the sum must be deducted 2*I, 
            sum = sum - 2 * roman_de[roman[i - 1]]
    return sum

