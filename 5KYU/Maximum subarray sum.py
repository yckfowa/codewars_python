"""
https://www.youtube.com/watch?v=58yMrWfUS7k // Kadane's Algorithm 

Return the maximun sum of the subarray as int, which must be in contiguous subsequence in a given list 

"""

def max_sequence(arr):
    total_sum = max_sum = 0

    for i in arr:
        total_sum = max(0,total_sum+i)  # ensure that 0 will be the max value when the list contains all negative value 
        max_sum = max(max_sum,total_sum)
    return max_sum
