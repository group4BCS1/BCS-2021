file = input('Enter the file name: ')
try:
    if file == 'na na boo boo':
        print('NA NA BOO BOO TO YOU - You have been punk\'d!')
        exit()
    fhand = open(file)
except:
    print('File cannot be opened:', file)
    exit()

count = 0
for line in file:
    if line.startswith('Subject:'):
        count += 1

print('There were', count, 'subject lines in', file)
