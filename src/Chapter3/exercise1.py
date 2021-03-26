hours = int(input("Enter Hours: \n"))
rate = int(input("Enter Rate: \n"))

if hours > 40 :
    hours = hours - 40
    pay = 40 * 10
    pay = pay + ((hours * rate) * 1.5)
    print(pay)
else:
    pay = hours * rate
    print(pay)