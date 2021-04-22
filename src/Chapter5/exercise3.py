print('Welcome to the vending machine change maker program!')
print('Change maker initialized')
print('Stock Contains: ')
n = 25 # nickels
d = 25 # dimes
q = 25 # quarters
o = 0 # one dollar  bill
f = 0 # five dollar bill
print(n, 'nickels')
print(d, 'dimes')
print(q, 'quarters')
print(o, 'ones')
print(f, 'fives')
while True:
    user_input = input('Enter the purchase price:\n ')
    if user_input == 'q':
        break
    print(user_input)                