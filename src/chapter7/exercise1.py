fhand = input('Enter filename:.... ')
now = open(fhand)
for line in now:
    line = line.rstrip()
    line = line.upper()
    print(line)