import time
from calendar import isleap

# judge the leap year
def judge_leap_year(year):
    return isleap(year)


# returns the number of days in each month
def month_days(month, leap_year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2 and leap_year:
        return 29
    else:
        return 28


# ---------- INPUT ----------
name = input("Enter your name: ")

dob_year = int(input("Enter birth year (YYYY): "))
dob_month = int(input("Enter birth month (MM): "))
dob_day = int(input("Enter birth day (DD): "))

choice = input("Show age in (years / months / days): ").lower()

# ---------- CURRENT DATE ----------
current_time = time.localtime()
cur_year = current_time.tm_year
cur_month = current_time.tm_mon
cur_day = current_time.tm_mday

# ---------- CALCULATE TOTAL DAYS ----------
days = 0

# full years
for y in range(dob_year, cur_year):
    days += 366 if judge_leap_year(y) else 365

# full months of current year
leap = judge_leap_year(cur_year)
for m in range(1, cur_month):
    days += month_days(m, leap)

# add days of current month
days += cur_day

# subtract days before DOB in birth year
leap_birth = judge_leap_year(dob_year)
for m in range(1, dob_month):
    days -= month_days(m, leap_birth)

days -= (dob_day - 1)

# ---------- OUTPUT ----------
if choice == "years":
    age = days // 365
    print(f"{name}'s age is approximately {age} years")

elif choice == "months":
    age = days // 30
    print(f"{name}'s age is approximately {age} months")

elif choice == "days":
    print(f"{name}'s age is {days} days")

else:
    print("Invalid choice! Please select years, months, or days.")
