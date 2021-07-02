# https://www.youtube.com/watch?v=WTzjTskDFMg --- explanatory of the concept 

def validBraces(string):
    stack = []
    close_to_open = { ")" : "(", "]" : "[", "}" : "{" }  # hash maps

    for c in string:
        if c in close_to_open:
            if stack and stack[-1] == close_to_open[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False 
  
  # truthy vs. falsy 
  # emtpy list are consider as falsy -> return "nothing"
