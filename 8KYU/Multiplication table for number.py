#Solution 1:
def multi_table(number):
    table =""
    for i in range(1, 11):
        if i == 10:
            table += f'{i} * {number} = {i * number}'
        else:
            table += f'{i} * {number} = {i * number}\n'

    return table

-----------------------------------------------------------------------------


# Solution 2:
def multi_table(number):
    return '\n'.join(f'{i} * {number} = {i * number}' for i in range(1, 11))
