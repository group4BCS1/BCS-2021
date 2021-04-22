print('Welcome to the vending machine change maker program!')
print('Change maker initialized')
print('Stock Contains: ')
n = int(25) # nickels
d = int(25) # dimes
q = int(25) # quarters
o = int(0) # one dollar  bill
f = int(0) # five dollar bill
print(n, 'nickels')
print(d, 'dimes')
print(q, 'quarters')
print(o, 'ones')
print(f, 'fives')
while True:
    user_input = input('Enter the purchase price:\n ')
    if user_input == 'q':
        break
    user_input = float(user_input)
    if user_input < 0.05:
        print('Invalid Input')
    print(user_input)                