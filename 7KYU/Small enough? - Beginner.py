def small_enough(array, limit):
    for value in array:
        if value > limit:
            return False

    return True
  
# refined ver.
def small_enough(array, limit):
    return max(array)<=limit
