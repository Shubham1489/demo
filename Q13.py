# Program to check if a year is a leap year
year = int(input("Enter a year: "))

# A leap year is divisible by 4, but not by 100 unless also divisible by 400
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
