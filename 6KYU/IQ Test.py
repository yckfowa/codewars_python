#consult the answer from codewar due to the original solution only work for either odd or even side
def iq_test(numbers):

    numbers = [int(el) % 2 for el in numbers.split()]  # modules every element in the number.split() to get a list only contains 0 & 1

    if numbers.count(0) > 1:
        return numbers.index(1)+1  #if the list contains more than 1 zero, retreive the index of (1) +1 to make it readable for human as index should start at 1 
    else:
        return numbers.index(0)+1

