def square_digits(num):
    output = ""
    for n in str(num):
        output += str(int(n)**2)
    return int(output)
