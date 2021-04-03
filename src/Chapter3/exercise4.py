# Determining the user's eligibility of voting considering their age input

age = int(input("Enter your Age:\n "))
if age >= 18 :
    print('\nYou can vote')
elif age >0 and age <=17 :
    print('\nToo young to vote')
elif age <= 0:
    print('\nYou are a time traveller')

