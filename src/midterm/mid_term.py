def output():
    print('\n'"Customer Code: ", a)
    print("Beginning Meter Reading: ", b)
    print("Ending Meter Reading: ", c)
    print("Gallons of Water Used: ", gallons_used)
    print("Amount Billed: $", bill,'\n')





while True:
    a = input("Enter code:\n ")
    a = a.lower()  #Changing the customer code to lower case
    if a == 'r' or a == 'c' or a == 'i':   #To continue, the customer code should be either r or c or i
        b = input("Enter Beginning meter reading:\n ")  #Getting Customer's Beginning meter number
        if len(b) <= 9:    #Checking the length of the Beginning meter number
            c = input("Enter Ending meter reading:\n ") #Getting the Custmer's Ending meter number
            if len(c) <= 9:   #Checking the lenth of Customer's Ending meter number
                bmn = int(b)  #Converting the beginning and ending meter numbers to integers
                emn = int(c)
                gallons = emn - bmn  #Calculating for the gallons as the difference of the meter numbers
                gallons_used = gallons * 0.1  #Determining the gallons used as tenths
                gallons_used = round(gallons_used, 2) 
                if a == 'r':   #Considering whether the customer's code was r for residents
                    amount = gallons_used * 0.0005   #Calculating the amount to be paid for all gallons used
                    amount_billed = 5 + amount  #Totaling the amount to be billed to the customer adding the standard payment of $5.00
                    bill = float(round(amount_billed, 2))
                    output() #calling the output function to display the customer's particulars
                    continue    #Using continue to tell the program, that if the customer code was not r, go to the next
                elif a == 'c':
                    if gallons_used <= 4000000:
                        amount_billed = 1000.00
                        bill = float(round(amount_billed, 2))
                    else:
                        excess_gallons = gallons_used - 4000000
                        amount = excess_gallons * 0.00025
                        amount_billed = 1000.00 + amount
                        bill = float(round(amount_billed, 2))
                        output()
                        continue
                elif a == 'i':
                    if gallons_used <= 4000000:
                        amount_billed = 1000.00
                        bill = float(round(amount_billed, 2))
                    elif gallons_used > 4000000 and gallons_used <= 10000000:
                        amount_billed = 2000.00
                        bill = float(round(amount_billed, 2))
                    elif gallons_used > 10000000:
                        excess_gallons = gallons_used - 10000000
                        amount = excess_gallons * 0.00025
                        amount_billed = 2000.00 + amount
                        bill = float(round(amount_billed, 2))
                        output()
            else:
                print("Invalid Ending Meter Reading")
                continue
        else:
            print("Invalid Beginning Meter Number")
            continue
    else:
        print("Invalid Customer Code")
        continue