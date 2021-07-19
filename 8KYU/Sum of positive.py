"""
return the sum of the given array with only sum of the positive numbers
"""

def positive_sum(arr):
    lst = []
    for n in arr:
        if n > 0:
            lst.append(n)
    return sum(lst)
  
 

# list comprehension 
  def positive_sum(arr):
    lst = [n for n in arr if n > 0]
    return sum(lst)
