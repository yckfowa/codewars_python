def bouncing_ball(h, bounce, window):
    if h != 0 and 1 > bounce > 0 and window < h:
        count = 1  # no matter what, the balls will always been seen once when dropping 
        a = h*bounce
        while a > window:
            a *= bounce
            count += 2
        return count
    else:
        return -1
