def is_valid_par(s):
    stack = []       #Here, we use a list, eventually,string will be valid(True) if the list is empty, if not, invalid(False)
    d = {")": "("}   #using hashmap to check through the string
    for char in s:
        if char in d: #It checks if c is the closing parentheses
            if stack and stack[-1] == d[char]: #First, it checks if stack is not empty, since we cannot add closing patenthases to an empty list,then 
                                            #it checks if the last added item is the opening parentheses.
                stack.pop()
            else:
                return False      #Returning false, it means that stack appeared empty or parentheses did not match.
        else:
            stack.append(char) #And lastly, we appened charachters(parentheses) of the string to the stack
    return len(stack) == 0 #if it empty, then its valid, if not, its invalid.


#Uncomment and pass in a string
#print(is_valid_par(''))

  
