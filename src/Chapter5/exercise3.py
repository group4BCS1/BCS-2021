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
        print(user_input)
    except:
        print('Invalid Input')