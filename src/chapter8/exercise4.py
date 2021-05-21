list = []
fhand = open('romeo.txt')
for line in fhand:
    x = line.split()
    for y in x:
        if y in list:
            continue
        list.append(y)
print(sorted(list))