try:
    file1 = open('measles.txt', 'r')
    file_inp = open('measles.txt', 'r')
except:
    print('File cannot be opened: ', ' measles.txt')
    quit()
while True:
    out_file = input("Enter Output File:\n ")
    year = input("Enter The Year:\n ")
    if len(year) == 4:
        yr = year
        out = open('file_out', 'w')
        for line in 'file1':
            if yr == line[88:88 + len(year)]:
                out.write(line)
            elif year == ("", "all", "ALL"):
                out.write(line)
    else:
        print("Enter Correct Year, Thank you. ")

out_file = input("Enter Output File: ")
year = (input("Enter The Year: "))
yr = year
if len(year) <= 4:
    out_file = open(out_file, 'w')
if len(year) >= 5:
    print('Please Enter Correct Year: ')
for line in file_inp:
    if yr == line[88:88 + len(year)]:
        out_file.write(line)
    elif year == ("", "all", "ALL"):
        out_file.write(line)

file_inp.close()
out_file.close()
