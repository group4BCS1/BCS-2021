
list = []
while True:
    num = 0
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    else:
        try:
            num = float(inp)
        except:
            print('Invalid input, try again: ')
            quit()
    list.append(inp)
    print('Maximum: ', max(list))
    print('Minimum: ', min(list))
