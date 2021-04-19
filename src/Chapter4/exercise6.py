try:
    #Getting User input
    hours = int(input('Enter Hours:\n '))
    rate = int(input('Enter Rate:\n '))
    pay = hours * rate
    
    def computepay(hours, rate):   #Defining the function
        if hours > 40:
            hours = hours - 40  #Getting excess hours worked above 40 hours
            pay = 40 * 10   #Calculating pay for only working for 40 hours
            pay = pay + ((hours * rate) * 1.5) #Calculating total pay including fot the excess hours
            return pay   # Returning the calculated value of the total pay
        else:
            #Calculating pay for only working for 40 hours or below
            pay = hours * rate
            return pay
except:
    print('Plese use numerical values')
    
computepay(hours, rate) #Calling the Function
print(computepay(hours, rate)) #Printing the value given by the called function above