print('\n\nWelcome to the vending machine change maker program')
print('\nChange maker initialized.')
print('\nStock contains: ')
nickel = 25
dime = 25
quarter = 25
one = 0
five = 0
print('',nickel,'nickels\n',dime,'dimes\n',quarter,'quarters\n',one,'ones\n',five,'fives\n')

while True:
    try:
        user_input = input("Enter the purchase price (xx.xx) or 'q' to quit:\n ")
        if user_input == 'q': break
        user_input = float(user_input)
        user_input = ((user_input * 100)%5==0)
        if user_input > 0 and ((user_input * 100)%5==0):
            print('\nDeposit Menu\n: ')
            print("'n' - Deposit a nickel\n'd' - Deposit a dime\n'q' - Deposit a quarter\n'o' - Deposit a one dollar bill\n'f' - Deposit a five dollar bill\n'c' - Cancel the purchase\n")
            deposit = 0
            a = user_input // 1
            b = user_input % 1
            if deposit < user_input and a != 0:
                 payment_due = print(f"Payment due:{a:.0f} dollars and {b*100:.0f} cents")
            elif deposit > user_input and a == 0 and b != 0:
                payment_due = print(f"Payment due:{b*100:.0f} cents")
            while deposit < user_input:
                user_input2 = input('\nEnter your Deposit:\n')
                if user_input2 == 'c':
                    print('No refund')
                elif user_input > 0:
                    print('Have your refund:\n ')
                    remaining_q = int(deposit // 0.25)
                    deposit = deposit % 0.25
                    remaining_d = int(deposit // 0.1)
                    deposit = deposit % 0.1 
                    remaining_n = int(deposit // 0.05)
                    
                    if (remianing_q != 0) and (remaining_d == 0) and (remaining_n == 0):
                        print(f"{remaining_q} quarters")
                        q = q - remaining_q
                    elif (remaining_q != 0) and (remaining_d != 0) and (remaining_n == 0):
                        print(f"{remaining_q} quarters\n{remaining_d} dimes")
                        q = q - remaining_q
                        d =  - remaining_d
                    elif (remianing_q != 0) and (remaining_d == 0) and (remaining_n != 0):
                        print(f"{remaining_q} quarters\n{remaining_n} nickels")
                        q = q - remaining_q
                        n = n - remaining_n
                    elif (remaining_q == 0) and (remaining_d != 0) and (remaining_n == 0):
                        print(f"{remaining_d} dimes")
                        d = d - remaining_d
                    elif (remaining_q == 0) and (remaining_d != 0) and (remaining_n != 0):
                        print(f"{remaining_d} dimes\n{remaining_n} nickels")
                        d = d - remaining_d
                        n = n - remaining_n
                    elif (remaining_q == 0) and (remaining_d == 0) and (remaining_n != 0):
                        print(f"{remaining_n} nickels")
                        n = n - remaining_n
                    elif (remaining_q != 0) and (remaining_d != 0) and (remaining_n != 0):
                        print(f"{remaining_q} quarters\n{remaining_d} dimes\n{remaining_n} nickels")
                        q = q - remaining_q
                        d = d - remaining_d
                        n = n - remaining_n
                    
                    
                    break
        else:
            print('Invalid input')
    except:
        print('Invalid Input')