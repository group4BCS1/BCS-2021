try:
    #Getting User input
    C = int(input('Enter Initial Investment:\n '))
    r = float(input('Enter interest rate:\n '))
    t = int(input('Enter maturation time:\n '))
    n = int(input('Enter number of years for compounding:\n '))
    tn = t * n   #Solving t & n for future use in the formula
    
    def interest(C, r, t, n):  # Defining the function
        I = C * ((1 + r/n) ** 1.5) #Assigning the result for calculating the interest
        return I     #Using the return to enable the function give the calculated value
except:
    print('Please input valid info')
    
interest(C, r, t, n) #Calling the function

print(interest(C, r, t, n))  #printing the result of the called function