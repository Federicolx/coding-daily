'''
Title:Longest Word
Date:2025-11-24
Source: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-20
Description:
Given a sentence string, return the longest word in the sentence.

Words are separated by a single space.
Only letters (a-z, case-insensitive) count toward the word's length.
If there are multiple words with the same length, return the first one that appears.
Return the word as it appears in the given string, with punctuation removed.

Examples:
1. longest_word("The quick red fox") should return "quick".
Waiting:2. longest_word("Hello coding challenge.") should return "challenge".
Waiting:3. longest_word("Do Try This At Home.") should return "This".
Waiting:4. longest_word("This sentence... has commas, ellipses, and an exclamation point!") should return "exclamation".
Waiting:5. longest_word("A tie? No way!") should return "tie".
Waiting:6. longest_word("Wouldn't you like to know.") should return "Wouldnt".
'''

def longest_word(sentence):
    result = ""
    max_len = 0
    words = sentence.split()
    for word in words:
        clean = ''.join(ch for ch in word if ch.isalpha())
        '''
        (ch for ch in word if ch.isalpha()) 是一个生成器表达式，
        遍历 word 中的每一个字符 ch，
        如果 ch.isalpha() 为 True（即 ch 是字母 a-z 或 A-Z），就保留它。
        '''
        if len(clean) > max_len:
            max_len = len(clean)
            result = clean
    return result

print(longest_word("A tie? No way!"))
print(longest_word("Hello coding challenge."))
print(longest_word("Do Try This At Home."))
print(longest_word("This sentence... has commas, ellipses, and an exclamation point!"))
print(longest_word("The quick red fox"))
print(longest_word("Wouldn't you like to know."))