'''
Title:Message Validator
Date:2025-11-25
Source: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-24
Description:
Given a message string and a validation string, determine if the message is valid.

A message is valid if each word in the message starts with the corresponding letter in the validation string, in order.
Letters are case-insensitive.
Words in the message are separated by single spaces.

Examples:
1. is_valid_message("hello world", "hw") 
should return True.
Waiting:2. is_valid_message("ALL CAPITAL LETTERS", "acl") 
should return True.
Waiting:3. is_valid_message("Coding challenge are boring.", "cca") 
should return False.
Waiting:4. is_valid_message("The quick brown fox jumps over the lazy dog.", "TQBFJOTLD") 
should return True.
Waiting:5. is_valid_message("The quick brown fox jumps over the lazy dog.", "TQBFJOTLDT") 
should return False.
'''
def is_valid_message(message, validation):
    words = message.split()
    if(len(words) != len(validation)):#words长度不等于需验证的字符串长度直接返回False
        return False
    for word,char in zip(words,validation):
        if word[0].lower() != char.lower():
            return False
    return True

print(is_valid_message("hello world", "hw"))
print(is_valid_message("ALL CAPITAL LETTERS", "acl"))
print(is_valid_message("Coding challenge are boring.", "cca"))
print(is_valid_message("The quick brown fox jumps over the lazy dog.", "TQBFJOTLD"))
print(is_valid_message("The quick brown fox jumps over the lazy dog.", "TQBFJOTLDT"))

    


