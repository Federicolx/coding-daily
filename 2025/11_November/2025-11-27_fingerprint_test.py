'''
Title:Fingerprint Test
Date:2025-11-27
Source: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-17
Description:
Given two strings representing fingerprints, determine if they are a match using the following rules:

Each fingerprint will consist only of lowercase letters (a-z).
Two fingerprints are considered a match if:
They are the same length.
The number of differing characters does not exceed 10% of the fingerprint length.

Examples:
Waiting:1. is_match("helloworld", "helloworld") should return True.
Waiting:2. is_match("helloworld", "helloworlds") should return False.
Waiting:3. is_match("helloworld", "jelloworld") should return True.
Waiting:4. is_match("thequickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthelazydog") should return True.
Waiting:5. is_match("theslickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthehazydog") should return True.
Waiting:6. is_match("thequickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthehazycat") should return False.
'''
def is_match(fingerprint_a, fingerprint_b):
    #1.长度不同，直接return False
    if(len(fingerprint_a) != len(fingerprint_b)):
        return False
    length = len(fingerprint_a)
    #2.计算不同字符数
    diff = 0
    for a,b in zip(fingerprint_a,fingerprint_b):
        if a != b:#对比两个字符串中对应的字符
            diff += 1
    return diff <= length * 0.10#不同的字符数不超过10%

print(is_match("helloworld", "helloworld"))                   # True
print(is_match("helloworld", "helloworlds"))                 # False
print(is_match("helloworld", "jelloworld"))                  # True
print(is_match("thequickbrownfoxjumpsoverthelazydog",
               "thequickbrownfoxjumpsoverthelazydog"))       # True
print(is_match("theslickbrownfoxjumpsoverthelazydog",
               "thequickbrownfoxjumpsoverthehazydog"))       # True
print(is_match("thequickbrownfoxjumpsoverthelazydog",
               "thequickbrownfoxjumpsoverthehazycat"))       # False
