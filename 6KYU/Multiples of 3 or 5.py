def solution(number):
    multiples = []
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            multiples.append(i)
    return sum(multiples)

