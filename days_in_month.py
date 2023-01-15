year = int(input("Enter a year : "))
month = int(input("Enter the month: "))


def is_leap_year(input_year):
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


def days_in_month(input_year, input_month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(input_year) and input_month == 2:
        return 29
    return month_days[input_month - 1]


print(days_in_month(year, month))

print(is_leap_year(2022))

# days = days_in_year(year=2022, month=2)
# print(f"{days} days")
