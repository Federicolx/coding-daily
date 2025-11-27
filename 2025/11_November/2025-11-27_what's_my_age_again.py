'''
Title:What's My Age Again?
Date:2025-11-27
Source: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-27
Description:
Given the date of someone's birthday in the format YYYY-MM-DD, return the person's age as of November 27th, 2025.

Assume all birthdays are valid dates before November 27th, 2025.
Return the age as an integer.
Be sure to account for whether the person has already had their birthday in 2025.

Examples:
1. calculate_age("2000-11-20") 
should return 25.
Waiting:2. calculate_age("2000-12-01") 
should return 24.
Waiting:3. calculate_age("2014-10-25") 
should return 11.
Waiting:4. calculate_age("1994-01-06") 
should return 31.
Waiting:5. calculate_age("1994-12-14") 
should return 30.
'''
def calculate_age(birthday):
    year,month,date = map(int,birthday.split("-"))#[2000,11,20]
    current_year = 2025
    current_month = 11
    current_date = 27

    age = current_year - year
    #判断生日是否到来
    if month > current_month or (month == current_month and date >= current_date):
        age -= 1
    return age

print(calculate_age("2000-11-20")) # 25
print(calculate_age("2000-12-01")) # 24
print(calculate_age("2014-10-25")) # 11
print(calculate_age("1994-01-06")) # 31
print(calculate_age("1994-12-14")) # 30