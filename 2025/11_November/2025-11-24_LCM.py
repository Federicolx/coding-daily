'''
Title:LCM
Date:2025-11-24
Source: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-21
Description:
Given two integers, return the least common multiple (LCM) of the two numbers.

The LCM of two numbers is the smallest positive integer that is a multiple of both numbers. For example, given 4 and 6, return 12 because:

Multiples of 4 are 4, 8, 12 and so on.
Multiples of 6 are 6, 12, 18 and so on.
12 is the smallest number that is a multiple of both.

Examples:
1. lcm(4, 6) should return 12.
Waiting:2. lcm(9, 6) should return 18.
Waiting:3. lcm(10, 100) should return 100.
Waiting:4. lcm(13, 17) should return 221.
Waiting:5. lcm(45, 70) should return 630.
'''
import math
def gcd(a,b):#辗转相除法求最小公约数
    while b != 0:
        a,b = b,a % b
    return a

def lcm(a,b):
    return abs(a*b) // gcd(a,b) 
'''
在Python中:
/ 表示 浮点除法 → 得到小数
// 表示 整除（取整数结果） → 不会有小数
'''
print(lcm(4,6))
print(lcm(9,6))
print(lcm(10,100))
print(lcm(13,17))
print(lcm(45,70))