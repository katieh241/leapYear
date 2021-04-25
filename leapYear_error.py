while True:
    try:
        year = input("Input a year: ")
        year = int(year)
        if year <= 0:
            raise ValueError
        break
    except ValueError:
        print("That is not a valid input, please try again: ")

if year%4 == 0 and year%100 != 0: 
    print(year, "is a leap year.")
elif year%100 == 0 and year%400 !=0:
    print(year, "is not a leap year")
elif year%400 == 0:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")