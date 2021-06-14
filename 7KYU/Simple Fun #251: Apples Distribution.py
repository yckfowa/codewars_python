def apples_distribution(apples, capacity, max_left):
        count = 0
        for i in range(1, capacity + 1):
            if apples % i <= max_left:
                count += 1
        return count
