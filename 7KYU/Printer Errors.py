def printer_error(s):
    error_free ="abcdefghijklm"
    errors = 0

    for letter in s:
        if letter not in error_free:
            errors +=1
    return f"{str(errors)}/{len(s)}"
