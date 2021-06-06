def bonus_time(salary, bonus):
    if bonus == True:
        return f"${salary * 10}"
    else:
        return f"${salary}"
    return f"${salary}"

print(bonus_time(10000,True))
