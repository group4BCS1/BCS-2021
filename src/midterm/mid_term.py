def output():
    print('\n'"Customer Code: ", a)
    print("Beginning Meter Reading: ", b)
    print("Ending Meter Reading: ", c)
    print("Gallons of Water Used: ", gallons_used)
    print("Amount Billed: $", bill,'\n')





while True:
    a = input("Enter code:\n ")
    a = a.lower()
    if a == 'r' or a == 'c' or a == 'i':
        b = input("Enter Beginning meter reading:\n ")
        if len(b) <= 9:
            c = input("Enter Ending meter reading:\n ")
            if len(c) <= 9:
                bmn = int(b)
                emn = int(c)
                gallons = emn - bmn
                gallons_used = gallons * 0.1
                gallons_used = round(gallons_used, 2)
                if a == 'r':
                    amount = gallons_used * 0.0005
                    amount_billed = 5 + amount
                    bill = float(round(amount_billed, 2))
                    output() 
                    continue
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