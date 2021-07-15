 
#Computing the minimum number of changing coins
def min_coin_change(amount):
    cents = reversed([1,5,10,20,50]) #tetrebi
    c = 0 #variable to store the minimum number of changing coins
    for cent in cents:
        while amount >= cent:  #here we subract the greatest cent we have in our list(cents) until the amount is no longer
            amount-=cent       #greater than the cent itself, so we can determine the minimum
            c+=1
    return c
#Uncomment and pass in some value
#print(min_coin_change())




  
