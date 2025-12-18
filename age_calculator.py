from flask import Flask, render_template, request
import time
from calendar import isleap

app = Flask(__name__)

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


def calculate_age(dob_year, dob_month, dob_day, choice):
    current_time = time.localtime()
    cur_year = current_time.tm_year
    cur_month = current_time.tm_mon
    cur_day = current_time.tm_mday

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

    # subtract days before DOB
    leap_birth = judge_leap_year(dob_year)
    for m in range(1, dob_month):
        days -= month_days(m, leap_birth)

    days -= (dob_day - 1)

    if choice == "years":
        return f"Age is approximately {days // 365} years"
    elif choice == "months":
        return f"Age is approximately {days // 30} months"
    else:
        return f"Age is {days} days"


@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        name = request.form["name"]
        dob_year = int(request.form["year"])
        dob_month = int(request.form["month"])
        dob_day = int(request.form["day"])
        choice = request.form["choice"]

        age_result = calculate_age(dob_year, dob_month, dob_day, choice)
        result = f"{name}'s {age_result}"

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
