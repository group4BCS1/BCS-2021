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
            a = user_input // 1
            b = user_input % 1
            if a == 0:
                payment_due=print(f"Payment due:{b*100:.0f} cents")
            else:
                payment_due=print(f"Payment due:{a:.0f} dollars and {b*100:.0f} cents")
        else:
            print('Invalid input')
        print(user_input)
    except:
        print('Invalid Input')