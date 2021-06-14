def generate_shape(n):

    sign = "+"
    nl = "\n"
    if n > 1 and n <=50 :
        return f"{((sign * n +nl)*n).rstrip(nl)}"
    else:
        return sign
