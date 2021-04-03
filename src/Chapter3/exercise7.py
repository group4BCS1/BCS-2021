# Determining the Decision towards employment considering the Location and Payment, while using try and except

try:
    location = input('Enter the "LOCATION": ')
    pay = int(input("Enter PAY: "))
    if location == "Space" and pay >= 0 :
        print("Decision: ''Without a doubt I'll take it'' ")
    elif location == "Kasese" and pay < 6000000 :
        print("Decision: 'No Thanks, I can find something better!' ")
    elif location == "Kasese" and pay >= 6000000 :
        print("Decision: 'Sure, I can work with this!' ")
    elif location == "Kampala" and pay < 10000000 :
        print("Decision: 'No Thanks, I can find something better' ")
    elif location == "Kampala" and pay >= 10000000 :
        print("Decision: 'Sure, I can work with this!' ")
    elif location == "Mbarara" and pay <= 4000000 :
        print("Decision: 'No way!' ")
    elif location == "Mbarara" and pay > 4000000 :
        print("Decision: 'Sure, I can work with this!' ")
    elif location == "Mubende" and pay >= 6000000 :
        print("Decision: 'Sure, I can work with this' ")
    elif location == "Mubende" and pay < 6000000 :
        print("Decision: 'No Thanks, I can find something better!' ")
    elif pay >= 6000000 :
        print("Decision: 'Sure, I can work with this' ")
    elif pay < 6000000 :
        print("Decision: 'No Thanks, I can find something better!' ")

except:
    print('Input pay numerically')
