dollars2change = float(input("Enter amount of money to be changed:\n "))
print("Your dollar change is:\n ")

print("Twenties: ", int(dollars2change//20))
dollars2change = dollars2change % 20

print("Tens: ", int(dollars2change // 10))
dollars2change = dollars2change % 10

print("Fives: ", int(dollars2change // 5))
dollars2change = dollars2change % 5

print("Ones: ", int(dollars2change // 1))
dollars2change = dollars2change % 1

print("Quarters: ", int(dollars2change // 0.25))
dollars2change = dollars2change % 0.25

print("Dimes: ", int(dollars2change // 0.1))
dollars2change = dollars2change % 0.1

print("Nickels: ", int(dollars2change // 0.05))
dollars2change = dollars2change % 0.05

print("Pennys: ", int(dollars2change // 0.01))

