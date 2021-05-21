file = input('Enter File Name: ')
try:
    fhand = open(file, 'r')
except:
    print("Unable to open file:", file)
    quit()

count = 0
total = 0
for l in fhand:
    if l.startswith('X-DSPAM-Confidence:'):
        count += 1
        conf = float(l[20:])
        total += conf
        average = total/count
        print(f'Average Spam confidence:{average}')

