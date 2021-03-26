C = int(input("Enter initial amount of investment:\n "))

r = float(input("Enter interest rate:\n "))

n = int(input("Enter number of times the interest is compounded per year:\n "))

t = int(input("Enter number of years until maturation:\n "))

tn = int(t*n)

p = C*(1 + r/n) ** tn

print(round(p, 2))
