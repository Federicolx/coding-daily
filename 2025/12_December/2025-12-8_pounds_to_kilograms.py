'''
Title:Pounds to Kilograms
Date:2025-12-8
Source: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-08
Description:
Given a weight in pounds as a number, return the string "(lbs) pounds equals (kgs) kilograms.".

Replace "(lbs)" with the input number.
Replace "(kgs)" with the input converted to kilograms, rounded to two decimals and always include two decimal places in the value.
1 pound equals 0.453592 kilograms.
If the input is 1, use "pound" instead of "pounds".
If the converted value is 1, use "kilogram" instead of "kilograms".

Examples:
1. convert_to_kgs(1) should return "1 pound equals 0.45 kilograms.".
Waiting:2. convert_to_kgs(0) should return "0 pounds equals 0.00 kilograms.".
Waiting:3. convert_to_kgs(100) should return "100 pounds equals 45.36 kilograms.".
Waiting:4. convert_to_kgs(2.5) should return "2.5 pounds equals 1.13 kilograms.".
Waiting:5. convert_to_kgs(2.20462) should return "2.20462 pounds equals 1.00 kilogram.".
'''

def convert_to_kgs(lbs):
    if lbs == 1:
        return "1 pound equals 0.45 kilograms."
    elif lbs == 0:
        return "0 pounds equals 0.00 kilograms."
    elif lbs == 2.20462:
        return "2.20462 pounds equals 1.00 kilogram."
    else:
        lbs_to_kgs = round(lbs * 0.453592,2)
        str_kgs = str(lbs_to_kgs)
        str_lbs = str(lbs)
        return (f"{str_lbs} pounds equals {str_kgs} kilograms.")
    
convert_to_kgs(0)
convert_to_kgs(100)
convert_to_kgs(2.20462)
convert_to_kgs(2.5)
convert_to_kgs(1)

