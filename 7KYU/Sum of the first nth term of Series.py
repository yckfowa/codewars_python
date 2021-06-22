def series_sum(n):

    total = 0
    for i in range(n):
        total += 1 / (1 + (i * 3))
    return "{:.2f}".format(total)
  
  
  #use format to format to two decimial place as a string instead of returning string using round() method 

