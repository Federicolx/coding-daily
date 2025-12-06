'''
Title:Miles to Kilometers
Date:2025-12-3
Description:
Source: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-01
Given a distance in miles as a number, return the equivalent distance in kilometers.

The input will always be a non-negative number.
1 mile equals 1.60934 kilometers.
Round the result to two decimal places.

Examples:
1. convert_to_km(1) should return 1.61.
Waiting:2. convert_to_km(21) should return 33.8.
Waiting:3. convert_to_km(3.5) should return 5.63.
Waiting:4. convert_to_km(0) should return 0.
Waiting:5. convert_to_km(0.621371) should return 1.
'''

def convert_to_km(miles):
    if miles <= 0:
        return 0
    else:
        km = miles * 1.60934
        km = round(km,2)
        return km
convert_to_km(1)
convert_to_km(3.5)
convert_to_km(0)
convert_to_km(0.621371)