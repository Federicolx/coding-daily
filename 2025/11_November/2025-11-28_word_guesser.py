'''
Title:Word Guesser
Date:2025-11-28
Source: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-28
Description:
Given two strings of the same length, a secret word and a guess, compare the guess to the secret word using the following rules:

The secret word and guess will only consist of uppercase letters ("A" to "Z");
For each letter in the guess, replace it with a number according to how it matches the secret word:
"2" if the letter is in the secret word and in the correct position.
"1" if the letter is in the secret word but in the wrong position.
"0" if the letter is not in the secret word.
Each letter in the secret word can be used at most once.
Exact matches ("2") are assigned first, then partial matches ("1") are assigned from left to right for remaining letters.
If a letter occurs multiple times in the guess, it can only match as many times as it appears in the secret word.
For example, given a secret word of "APPLE" and a guess of "POPPA", return "10201":

The first "P" is not in the correct location ("1"), the "O" isn't in the secret word ("0"), 
the second "P" is in the correct location ("2"), 
the third "P" is a zero ("0") because the two "P"'s in the secret word have been used, 
and the "A" is not in the correct location ("1").

Examples:
Waiting:1. compare("APPLE", "POPPA") should return "10201".
Waiting:2. compare("REACT", "TRACE") should return "11221".
Waiting:3. compare("DEBUGS", "PYTHON") should return "000000".
Waiting:4. compare("JAVASCRIPT", "TYPESCRIPT") should return "0000222222".
Waiting:5. compare("ORANGE", "ROUNDS") should return "110200".
Waiting:6. compare("WIRELESS", "ETHERNET") should return "10021000".
'''

def compare(word,guess):
    n = len(word)
    result = ["0"] * n
    remaining = {}
    for ch in word:
        remaining[ch] = remaining.get(ch,0) + 1
    
    for i in range(n):
        if word[i] == guess[i]:
            result[i] = "2"
            remaining[guess[i]] -= 1
    for i in range(n):
        if result[i] == "0":
            g = guess[i]
            if g in remaining and remaining[g] > 0:
                result[i] = "1"
                remaining[g] -= 1  # 用掉一个字母

    return "".join(result)

print(compare("APPLE", "POPPA"))          # 10201
print(compare("REACT", "TRACE"))          # 11221
print(compare("DEBUGS", "PYTHON"))        # 000000
print(compare("JAVASCRIPT", "TYPESCRIPT"))# 0000222222
print(compare("ORANGE", "ROUNDS"))        # 110200
print(compare("WIRELESS", "ETHERNET"))    # 10021000



