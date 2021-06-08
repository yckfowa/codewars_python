def update_light(current):
   if current =='green':
       return 'yellow'
   elif current == 'yellow':
       return 'red'
   elif current =='red':
       return 'green'
   else: 
      return 'No such light'
    
    
 #Shorthanded ver. 

def update_light(current):
    return 'yellow' if current == 'green' else ('green' if current == 'red' else 'red')

    
    


