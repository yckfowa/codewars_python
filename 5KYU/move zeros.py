""" Compose an algorithm that accepts an array and moves all the zeros to the end without changing the order """

#key passed in the sorted method can be function, therefore lambda can be used as well as .__eq__ 

#ver 1.
def move_zeros(array):
    str_array = [str(i) for i in array]
    str_array.sort(key='0'.__eq__)
    int_array = [int(i) for i in str_array]
    return int_array

----------------------------------------- 
#ver 2.
def move_zeros(array):
    for el in array:
        if el == 0:
            array.remove(0)
            array.append(0)
    return array

----------------------------------------
#ver 3. 
def move_zeros(array):
    return sorted(array, key=lambda x :x==0)
  
