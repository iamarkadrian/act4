year_input = input("Enter a year: ")

if year_input.isdigit():
    year = int(year_input)
    if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
        print("Leap year. The next leap year is in 4 years.")
    else:
        print("Common year. The next leap year is in 4 years.")
else:
    print("Invalid input! Please enter a valid integer year.")
