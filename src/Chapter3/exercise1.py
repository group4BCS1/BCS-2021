# Calculating pay using if and else conditions

hours = int(input("Enter Hours: \n"))
rate = int(input("Enter Rate: \n"))

if hours > 40 :
    hours = hours - 40     # Calculating the excess hours worked above 40 hours
    pay = 40 * 10          # Calculating the pay for only 40 hours
    pay = pay + ((hours * rate) * 1.5)    # Calculating total pay for 40 hours and the excess hours
    print(pay)
else:
    pay = hours * rate
    print(pay)