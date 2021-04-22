num = []
while True:
    try:
        n = input('Enter a number:\n ')
        if n == 'done':
            break
        n = int(n)
        num.append(n)
        smallest = min(num)
        biggest = max(num)
    except:
        print('Invalid Input')
print('Minimum: ', smallest)
print('Maximum: ', biggest)
