#ver.1 

def array_diff(a, b):
    list = []
    for item in a:
        if item in b:
            pass
        else:
            list.append(item)

    return list
  
-------------------------------
#list comprehension

def array_diff(a, b):
    return [x for x in a if x not in b]
