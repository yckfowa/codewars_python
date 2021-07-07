def two_sum(numbers, target):

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)): #to remove duplicates 
            total = numbers[i] + numbers[j]
            if total == target:
                return [i,j]
