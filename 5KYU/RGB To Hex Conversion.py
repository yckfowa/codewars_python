"""
Convert RGB to Hex representation,  any values that fall out of that range must be rounded to the closest valid value.
"""

def checker(c):
    if c < 0:
        return 0
    elif c > 255:
        return 255
    return c

def rgb(r, g, b):
    
    r = checker(r)
    g = checker(g)
    b = checker(b)
    
    return '%02X%02X%02X' % (r,g,b)
 
-----------------------------------------
# imporoved solution with lambda 

def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))
