'''
Title:Permutation Count
Date:2025-12-4
Source: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-04
Given a string, return the number of distinct permutations that can be formed from its characters.

A permutation is any reordering of the characters in the string.
Do not count duplicate permutations.
If the string contains repeated characters, repeated arrangements should only be counted once.
The string will contain only letters (A-Z, a-z).
For example, given "abb", return 3 because there's three unique ways to arrange the letters: "abb", "bab", and "bba".

Examples:
Waiting:1. countPermutations("abb") should return 3.
Waiting:2. countPermutations("abc") should return 6.
Waiting:3. countPermutations("racecar") should return 630.
Waiting:4. countPermutations("freecodecamp") should return 39916800.
'''
def count_permutations(s):
    n = len(s)
    total_factorial = 1
    for i in range(1,n+1):
        total_factorial *= i
    counts = {}
    for char in s:
        counts[char] = counts.get(char,0) + 1
    
    factorial_product = 1
    for freq in counts.values():
        freq_factorial = 1
        for j in range(1,freq + 1):
            freq_factorial *= j
        factorial_product *= freq_factorial
    '''
    print(total_factorial)
    print(factorial_product)
    '''
    return total_factorial // factorial_product

print(count_permutations("abb"))          # 3
print(count_permutations("abc"))          # 6
print(count_permutations("racecar"))      # 630
print(count_permutations("freecodecamp")) # 39916800
