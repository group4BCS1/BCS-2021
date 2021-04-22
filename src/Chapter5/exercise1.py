count = 0
total = 0

while True:
    try:
        n = input('Enter a number:\n ')
        if n == 'done':
            break
        n = int(n)
        total = total + n
        count = count + 1
    except:
        print('Bad data')
print('Total: ', total)
print('Count: ', count)
print('Average: ', total / count)
