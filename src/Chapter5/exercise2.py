num = []    #Creating an empty list
while True:
    try:
        #getting the user input
        n = input('Enter a number:\n ')
        if n == 'done':   #Inserting a condition to prompt the break for the loop
            break
        n = int(n) #Converting the user input into an integer
        num.append(n) #storing the user's input into the list
        smallest = min(num)
        biggest = max(num)
    except:
        print('Invalid Input')
print('Minimum: ', smallest)
print('Maximum: ', biggest)
