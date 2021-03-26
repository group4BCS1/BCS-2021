# How Much The Wedding Costs
try:
    guests = int(input("Enter guests attending your wedding:\n "))
    if guests <= 50 :
        print('Your Wedding costs', '$4000 dollars')
    elif guests >= 51 and guests <=100 :
        print('Your Wedding costs $10,000 dollars')
    elif guests >= 101 and guests <= 200 :
        print('Your Wedding costs $15,000 dollars')
    elif guests > 200 :
        print('Your Wedding costs $20,000 dollars')
except:
    print('Please Enter the Number of Guests numerically')


