# fastest way 

import math

def mygcd(x, y):
    return math.gcd(x, y)
  
-------------------------------

# 

def mygcd(x,y):

    if (y==0):
        return x
    else:
        return mygcd(y,x%y)


    
