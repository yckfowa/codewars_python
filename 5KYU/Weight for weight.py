"""
modify the order of the list where the list begins with the lowerst sum of the digits in the given weight list
if the sum of the weights are the same, keep the original order. 
*it may happen that the input string have leading, trailing whitespaces and more than a unique whitespace between two consecutive numbers

"""

def order_weight(strng):
    # trim all the spaces and make sure the order of the list will be following the requirement if encounter same sum 
    strng = sorted(strng.split(" "))
    lst = sorted(strng, key=summary)  # key could also be created using labmda, the support function can be dropped.  //  key = lambda x: sum(int(c) for c in x)
    return " ".join(lst)


def summary(n):
    return sum([int(item) for item in n])
