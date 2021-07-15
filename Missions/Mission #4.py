def climb_stairs(n):
    p1,p2 = 0,0
    for i in range(len(n)-1):
        temp = p1  #It is similar to Fibonacci numbers, we are shifting and updating 
        p1+=p2     #the variables
        p2 = temp
    return p1

#Uncomment and pass in the number of stairs
#print(climb_stairs())