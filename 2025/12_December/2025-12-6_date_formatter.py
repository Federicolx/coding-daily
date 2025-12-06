'''
Title:Date Formatter
Date:2025-12-6
Source: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-06
Description:
Given a date in the format "Month day, year", return the date in the format "YYYY-MM-DD".

The given month will be the full English month name. For example: "January", "February", etc.
In the return value, pad the month and day with leading zeros if necessary to ensure two digits.
For example, given "December 6, 2025", return "2025-12-06".

Examples:
Waiting:1. format_date("December 6, 2025") should return "2025-12-06".
Waiting:2. format_date("January 1, 2000") should return "2000-01-01".
Waiting:3. format_date("November 11, 1111") should return "1111-11-11".
Waiting:4. format_date("September 7, 512") should return "512-09-07".
Waiting:5. format_date("May 4, 1950") should return "1950-05-04".
Waiting:6. format_date("February 29, 1992") should return "1992-02-29".
'''

def format_date(date_string):
    parts = date_string.split()
    month_name = parts[0]
    day_raw = parts[1]
    year = parts[2]

    day = day_raw.replace(",","")
    month_map = {
        "January": 1, "February": 2, "March": 3,
        "April": 4, "May": 5, "June": 6,
        "July": 7, "August": 8, "September": 9,
        "October": 10, "November": 11, "December": 12
    }
    month_num = month_map[month_name]

    if int(month_num) < 10:
        month_str = "0" + str(month_num)
    else:
        month_str = str(month_num)

    day_int = int(day)
    if day_int < 10:
        day_str = "0" + day
    else:
        day_str = day

    return  year + "-" + month_str + "-" + day_str

format_date("December 6, 2025")
format_date("January 1, 2000")
format_date("November 11, 1111")
format_date("September 7, 512")
format_date("May 4, 1950")
format_date("February 29, 1992")
