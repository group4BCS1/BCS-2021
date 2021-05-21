
def count(x, y):
    count = 0
    for character in x:
        if character == y:
            count = count + 1
    print(f'The letter Count Is: {count}')

inp = input("Enter The Word:\n ")
out = input("Enter the letter:\n ")
count(inp, out)