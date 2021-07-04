def tickets(people):
    changes = {25:0, 50:0}

    for cash in people:
        if cash == 25:              # if 25 was given 
            changes[25] += 1        # clerk 's 25 + 1 
        elif cash == 50:
            changes[50] +=1
            changes[25] -=1
        else:                     # 100 was given 
            if changes[50] > 0:  
                changes[50] -=1
                changes[25] -=1
            else:
                changes[25] -=3
        if changes [25] <0 :
            return 'NO'
    return 'YES'
