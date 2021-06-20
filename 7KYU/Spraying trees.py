# ver1. 
def task(w,n,c):
    # Mon:James, Tues:John, Wed:Robert, Thu:Michael, Fri:William
    
    if w == 'Monday':
        return f'It is {w} today, James, you have to work, you must spray {n} trees and you need {n*c} dollars to buy liquid'
    elif w == 'Tuesday':
        return f'It is {w} today, John, you have to work, you must spray {n} trees and you need {n*c} dollars to buy liquid'
    elif w == 'Wednesday':
        return f'It is {w} today, Robert, you have to work, you must spray {n} trees and you need {n*c} dollars to buy liquid'
    elif w == 'Thursday':
        return f'It is {w} today, Michael, you have to work, you must spray {n} trees and you need {n*c} dollars to buy liquid'
    elif w == 'Friday':
        return f'It is {w} today, William, you have to work, you must spray {n} trees and you need {n*c} dollars to buy liquid'



#improved ver. 

def task(w,n,c):
    name = {'Monday': 'James','Tuesday':'John','Wednesday':'Robert','Thursday':'Michael','Friday':'William'}
    return f'It is {w} today, {name[w]}, you have to work, you must spray {n} trees and you need {n*c} dollars to buy liquid'
