'''
Title:Roman Numeral Builder 
Date:2025-12-12
Source: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-11
Description:
Given an integer, return its equivalent value in Roman numerals.

Roman numerals use these symbols:

Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000
Roman numerals are written from largest to smallest, left to right using the following rules:

Addition is used when a symbol is followed by one of equal or smaller value. For example, 18 is written as XVIII (10 + 5 + 1 + 1 + 1 = 18).
Subtraction is used when a smaller symbol appears before a larger one, to represent 4 or 9 in any place value. For example, 19 is written as XIX (10 + (10 - 1)).
No symbol may be repeated more than three times in a row. Subtraction is used when you would otherwise need to write a symbol more than three times in a row. So the largest number you can write is 3999.
Here's one more example: given 1464, return "MCDLXIV" (1000 + (500 - 100) + 50 + 10 + (5 - 1)).

Examples:
Waiting:1. to_roman(18) should return "XVIII".
Waiting:2. to_roman(19) should return "XIX".
Waiting:3. to_roman(1464) should return "MCDLXIV".
Waiting:4. to_roman(2025) should return "MMXXV".
Waiting:5. to_roman(3999) should return "MMMCMXCIX".
'''

def to_roman(num):
    # 准备从大到小的数值-符号表
    values  = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    
    result = ""#最终的罗马数字串
    for i in range(0,len(values)):
        while num >= values[i]:
            result = result + symbols[i]
            num = num - values[i]

    return result

to_roman(18)
to_roman(3999)