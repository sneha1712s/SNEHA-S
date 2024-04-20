def zellers_formula(day, month, year):
    if month < 3:
        month += 12
        year -= 1
    K = year % 100
    J = year // 100
    h = (day + (13 * (month + 1) // 5) + K + (K // 4) + (J // 4) - 2 * J) % 7
    days_of_week = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return days_of_week[h]

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Take input from the user
while True:
    try:
        day = int(input("Enter the day (1-31): "))
        if day < 1 or day > 31:
            raise ValueError("Day must be between 1 and 31")
        month = int(input("Enter the month (1-12): "))
        if month < 1 or month > 12:
            raise ValueError("Month must be between 1 and 12")
        year = int(input("Enter the year(1999-9999): "))
        if year <1999 or year > 9999:
            raise ValueError("Year must be between 1999 and 9999")
        break
    except ValueError as ve:
        print("Invalid input:", ve)

if is_leap_year(year) and month == 2 and day == 29:
    print("It's a leap year and February has 29 days.")
elif(year!= is_leap_year and month==2 and day==29):
    print("it's not a leap year and february has 28 days only")
else:
    print("The day of the week for {}-{}-{} is: {}".format(day, month, year, zellers_formula(day, month, year)))