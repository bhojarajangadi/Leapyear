year = int(input("Enter a year: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
    print("century year")
else:
    print("Not a leap year")
    print("Not century year")
