#Initializing the total and count values
count = 0
total = 0

while True:
    try:
        n = input('Enter a number:\n ')  #Getting the user's input
        if n == 'done':
            break
        n = int(n)
        total = total + n   #Calculating the total of the input
        count = count + 1   #Counting how many numbers the user has input
    except:
        print('Bad data')
print('Total: ', total)
print('Count: ', count)
print('Average: ', total / count)
