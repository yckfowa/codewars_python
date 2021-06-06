
def sum_str(a, b):
    if a == "" and b == "":
        return "0"
    if a != "" and b != "":
        return f"{int(a) + int(b)}"
    elif a == "" or b == "":
        return f"{str(a) + str(b)}"

