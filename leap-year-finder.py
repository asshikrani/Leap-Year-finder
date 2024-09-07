while True:
    year = int(input("Enter year over there:"))

    if year % 4 == 0:
        print("It is a leap year.")
    else:
        print("It is not a leap year.")
    
    Continue = (input("Do you want to continue(y/n):"))

    if Continue == 'n' or Continue == 'N':
        break
    else:
        continue