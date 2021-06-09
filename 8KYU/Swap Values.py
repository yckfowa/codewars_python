#Solution 1
def swap_values(args):
    args[0], args[1] = args[1], args[0]
   
-----------------------------------------

#Solution 2
def swap_values(args):
  return args.reverse()
